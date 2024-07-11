class RomanConverter:
    convert_dict = {"I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000}

    def convert_to_arabic(self, roman_numerals):
        if len(roman_numerals) == 1:
            return self.convert_single_roman_to_arabic(roman_numerals)

        else:
            return self.convert_multiple_roman_to_arabic(roman_numerals)

    def convert_single_roman_to_arabic(self, roman_numeral):
        return self.convert_dict[roman_numeral]

    def convert_multiple_roman_to_arabic(self, roman_numerals):
        result = self.convert_single_roman_to_arabic(roman_numerals[-1])
        for i in range(len(roman_numerals) - 1, 0, -1):
            left_arabic_number = self.convert_single_roman_to_arabic(roman_numerals[i-1])
            right_arabic_number = self.convert_single_roman_to_arabic(roman_numerals[i])

            if left_arabic_number >= right_arabic_number:
                result += left_arabic_number
            else:
                result -= left_arabic_number

        return result
