import unittest
from roman_number import RomanNumber


class TestRomanNumber(unittest.TestCase):
    def test_roman_number_1(self):
        self.assertEqual(int(RomanNumber("III")), 3)
    def test_roman_number_2(self):
        self.assertEqual(int(RomanNumber("LVIII")), 58)
    def test_roman_number_3(self):
        self.assertEqual(int(RomanNumber("MCMXCIV")), 1994)