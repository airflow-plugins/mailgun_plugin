import requests

from airflow.hooks.base_hook import BaseHook


class MailgunHook(BaseHook):
    """
    ✉️🔫.
    """

    def __init__(self, mailgun_conn_id):
        self.mailgun_conn_id = mailgun_conn_id
        conn = self.get_connection(mailgun_conn_id)
        self.public_api_key = conn.login

        self.session = requests.Session()
        self.session.auth = ('api', self.public_api_key)

    def parse_emails(self, emails):
        """
        Parse a list of emails.
        """
        addresses = ','.join(emails)

        r = self.session.get(
            'https://api.mailgun.net/v3/address/parse',
            params={
                'addresses': addresses,
            },
        )
        resp = r.json()

        parsed = resp['parsed']
        unparseable = resp['unparseable']

        if len(unparseable) > 0:
            print(f'* warning: {len(unparseable)} unparseable emails')
        else:
            print(f'* no unparseable')

        return parsed, unparseable

    def validate_email(self, email):
        """
        Validate one email address.
        """
        r = self.session.get(
            'https://api.mailgun.net/v3/address/validate',
            params={
                'address': email,
            },
        )
        resp = r.json()
        return resp

    # def validate_emails(self, emails):
    #     """
    #     Validate multiple email addresses.

    #     There is currently no bulk validation endpoint.
    #     """
    #     print('* MailgunHook.validate_emails')
    #     resps = []
    #     for email in emails:
    #         resp = self.validate_email(email)
    #         resps.append(resp)
    #     return resps
