def is_likely_human(response):
    """
    From the email validation response, determine whether a given email is valid by combining the various signals in an opinionated way to return a boolean.

    This can be tweaked to be more/less aggressive.

    An individual response looks like this:

    {'address': 'Foo <foo@mailgun.net>',
     'did_you_mean': None,
     'is_disposable_address': False,
     'is_role_address': False,
     'is_valid': False,
     'mailbox_verification': None,
     'parts': {'display_name': None, 'domain': None, 'local_part': None},
     'reason': 'malformed address; failed parse checks'}
    """
    is_disposable = response['is_disposable_address']
    is_role = response['is_role_address']  # role ex. info@, postmaster@
    is_valid = response['is_valid']

    is_human = is_valid and not is_disposable and not is_role

    return is_human
