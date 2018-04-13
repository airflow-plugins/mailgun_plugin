"""
Airflow plugin for Mailgun email validation on contacts.

Note: The email validation API is _not free_ and charges per validation check,
not per email address, so we should be conscious of running more than once for
a given email.
"""

from airflow.plugins_manager import AirflowPlugin

from mailgun_plugin.operators import EmailListChangedSensor
from mailgun_plugin.operators import EmailValidationOperator


class MailgunPlugin(AirflowPlugin):
    name = 'mailgun_plugin'
    operators = [
        EmailListChangedSensor,
        EmailValidationOperator,
    ]
