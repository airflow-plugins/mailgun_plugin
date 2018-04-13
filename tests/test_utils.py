import unittest

from mailgun_plugin.utils import is_likely_human


class IsLikelyHumanTestCase(unittest.TestCase):

    def test_is_likely_human_valid(self):
        expected = True
        response = {
            'address': 'taylor@astronomer.io',
            'is_disposable_address': False,
            'is_role_address': False,
            'is_valid': True,
        }
        actual = is_likely_human(response)
        self.assertEqual(expected, actual)

    def test_is_likely_human_invalid(self):
        expected = False
        response = {
            'address': 'mark.zuckerberg@astronomer.io',
            'is_disposable_address': False,
            'is_role_address': False,
            'is_valid': False,
        }
        actual = is_likely_human(response)
        self.assertEqual(expected, actual)

    def test_is_likely_human_role(self):
        expected = False
        response = {
            'address': 'info@astronomer.io',
            'is_disposable_address': False,
            'is_role_address': True,
            'is_valid': True,
        }
        actual = is_likely_human(response)
        self.assertEqual(expected, actual)
