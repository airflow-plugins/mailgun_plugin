import datetime
import json

from airflow.hooks.S3_hook import S3Hook
from airflow.models import BaseOperator

from mailgun_plugin.hooks.mailgun_hook import MailgunHook
from mailgun_plugin.utils import filter_address_only
from mailgun_plugin.utils import is_likely_human
from mailgun_plugin.utils import json_serial
from mailgun_plugin.utils import parse_ndjson_from_contents


class EmailValidationOperator(BaseOperator):
    """
    An operator to validate email addresses via Mailgun.

    https://documentation.mailgun.com/en/latest/user_manual.html#email-validation
    """

    def __init__(self, mailgun_conn_id, aws_conn_id, s3_bucket_name,
                 s3_key_source, *args, **kwargs):
        # compute results via mailgun api
        self.mailgun_conn_id = mailgun_conn_id

        # fetch from and write to s3
        self.aws_conn_id = aws_conn_id
        self.s3_bucket_name = s3_bucket_name
        self.s3_key_source = s3_key_source

        super(EmailValidationOperator, self).__init__(*args, **kwargs)

    def get_hook(self):
        return MailgunHook(
            mailgun_conn_id=self.mailgun_conn_id,
        )

    def _get_s3_file_contents(self):
        # connect to s3
        s3_hook = S3Hook(aws_conn_id=self.aws_conn_id)

        # get file from s3
        if not s3_hook.check_for_key(self.s3_key_source,
                                     bucket_name=self.s3_bucket_name):
            raise Exception('S3 key {} does not exist in {}'.format(
                self.s3_key_source, self.s3_bucket_name))

        # read file
        s3_obj = s3_hook.get_key(self.s3_key_source,
                                 bucket_name=self.s3_bucket_name)
        s3_file_contents = s3_obj.get()['Body'].read().decode('utf-8')

        return s3_file_contents

    def execute(self, context):
        # one consistent timestamp for whole batch
        now = datetime.datetime.utcnow()

        s3_file_contents = self._get_s3_file_contents()
        objs = parse_ndjson_from_contents(s3_file_contents)

        emails = [x.email_address for x in objs]

        self.mailgun_hook = self.get_hook()

        parsed, unparseable = self.mailgun_hook.parse_emails(emails)

        addresses = [filter_address_only(x) for x in parsed]

        # self.mailgun_hook.validate_emails()
        results = []
        for email in addresses:
            resp = self.mailgun_hook.validate_email(email)
            human = is_likely_human(resp)
            result = {
                'email': email,
                'human': human,
                'response': resp,
                'last_validated': now,
            }
            results.append(result)

        # serialize results
        ndjson_output_content = '\n'.join([json.dumps(x, default=json_serial)
                                           for x in results])
        print(ndjson_output_content)
