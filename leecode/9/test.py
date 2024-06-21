import unittest
from number import Number


class TestPalindromeNumber(unittest.TestCase):
    def test_two_sum_1(self):
        self.assertTrue(Number(121).is_palindrome())
    def test_two_sum_2(self):
        self.assertFalse(Number(-121).is_palindrome())
    def test_two_sum_3(self):
        self.assertFalse(Number(10).is_palindrome())