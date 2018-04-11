import re


def filter_address_only(email):
    """
    The Mailgun parse API can return emails like: a@b.com, Foo <a@b.com>, Foo Bar <a@b.com>, etc; but the validate API needs just the email address component.

    This may be a bug in their API as they seemed surprised it didn't work when I mentioned it.
    """
    pattern_with_name = re.compile(r'.*<(.*)>.*')
    match1 = pattern_with_name.match(email)
    # print(f'match1={match1}')

    pattern_address_only = re.compile(r'.*@.*')
    match2 = pattern_address_only.match(email)
    # print(f'match2={match2}')

    if match1 is not None:
        email_address = match1.groups()[0]
    elif match2 is not None:
        email_address = match2.group()
    else:
        raise Exception('warning no regex match for email {}'.format(email))

    return email_address
