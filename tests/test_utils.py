from mailgun_plugin.utils import is_likely_human


def test_is_likely_human_valid():
    response = {
        'address': 'taylor@astronomer.io',
        'is_disposable_address': False,
        'is_role_address': False,
        'is_valid': True,
    }
    assert is_likely_human(response) is True


def test_is_likely_human_invalid():
    response = {
        'address': 'mark.zuckerberg@astronomer.io',
        'is_disposable_address': False,
        'is_role_address': False,
        'is_valid': False,
    }
    assert is_likely_human(response) is False


def test_is_likely_human_role():
    response = {
        'address': 'info@astronomer.io',
        'is_disposable_address': False,
        'is_role_address': True,
        'is_valid': True,
    }
    assert is_likely_human(response) is False
