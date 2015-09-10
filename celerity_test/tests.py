from django.test import TestCase
from numerals.views import calc_numerals


class RomanNumberalsTestCase(TestCase):
    def setUp(self):
        pass

    def test_conversion(self):
        """Convert integers up to 3999 to Roman numerals."""
        test_cases=dict(
            VI=6,
            IX=9,
            XVIII=18,
            XIX=19,
            XXXVIII=38,
            XXXIX=39,
            XL=40,
            XCVIII=98,
            CCCLXXXVIII=388,
            CDXCIX=499,
            DCCCLXVII=867,
            MCMXCVIII=1998,
            MMMCMXCIX=3999,
        )

        for roman_numerals, value in test_cases.items():
            self.assertEqual(calc_numerals(value), roman_numerals)
