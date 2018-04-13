import pytest

from mailgun_plugin.utils import is_likely_human


@pytest.mark.parametrize('address,disposable,role,valid,expected', [
    ('taylor@astronomer.io', False, False, True, True),
    ('mark.zuckerberg@astronomer.io', False, False, False, False),
    ('info@astronomer.io', False, True, True, False),
])
def test_is_likely_human(address, disposable, role, valid, expected):
    assert is_likely_human({
        'address': address,
        'is_disposable_address': disposable,
        'is_role_address': role,
        'is_valid': valid,
    }) is expected
