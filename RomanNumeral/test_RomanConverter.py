from unittest import TestCase

from RomanConverter import RomanConverter


class TestRomanConverter(TestCase):
    def setUp(self):
        self.converter = RomanConverter()

    def test_convert_single_roman_numerals(self):
        for roman_num, arabic_num in self.converter.convert_dict.items():
            with self.subTest(f"{roman_num} to {arabic_num}"):
                self.assertEqual(arabic_num, self.converter.convert_to_arabic(roman_num))

    def test_convert_length2_roman_numerals_right_high(self):
        lst = [(4, "IV"), (40, "XL"), (999, "IM"), (95, "VC")]
        for arabic_num, roman_num in lst:
            with self.subTest(f"{roman_num} to {arabic_num}"):
                self.assertEqual(arabic_num, self.converter.convert_to_arabic(roman_num))


    def test_convert_length2_roman_numerals_left_high(self):
        lst = [(6, "VI"), (60, "LX"), (1001, "MI"), (105, "CV")]
        for arabic_num, roman_num in lst:
            with self.subTest(f"{roman_num} to {arabic_num}"):
                self.assertEqual(arabic_num, self.converter.convert_to_arabic(roman_num))

