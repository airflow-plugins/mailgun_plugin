from pprint import pprint

import requests

from airflow.hooks.base_hook import BaseHook


class MailgunHook(BaseHook):
    """
    ✉️🔫.
    """

    def __init__(self, mailgun_conn_id):
        self.mailgun_conn_id = mailgun_conn_id
        conn = self.get_connection(mailgun_conn_id)
        # print('conn=', conn, conn.login, dir(conn), conn.__dict__)
        self.conn = conn
        self.public_api_key = self.conn.login
        # print('self.public_api_key=', self.public_api_key)

        self.session = requests.Session()
        self.session.auth = ('api', self.public_api_key)

    def parse_emails(self, emails):
        """
        Parse a list of emails.
        """
        addresses = ','.join(emails)

        r = self.session.get(
            'https://api.mailgun.net/v3/address/parse',
            # auth=('api', self._api_key),
            params={
                'addresses': addresses,
            },
        )
        resp = r.json()
        pprint(resp)

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
        print('* MailgunHook.validate_email')
        r = self.session.get(
            'https://api.mailgun.net/v3/address/validate',
            # auth=('api', self._api_key),
            params={
                'address': email,
            },
        )
        resp = r.json()
        pprint(resp)
        print()
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

    # def has_email_list_changed(self):
    #     print('* MailgunHook.has_email_list_changed')
    #     pass

    # def fetch_emails(self):
    #     print('* MailgunHook.fetch_emails')
