"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        pass

    def number_to_roman(num):
        val = [
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        if num == 0:
                return "The value 0 does not exist in Roman numerals."
        if num < 0:
                return "number can not less than 0"
        
        roman_num = ''
        i = 0
        while  num > 0:

            time = num // val[i]
            for j in range(time):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
    

    input_num = (int(input("Enter a number : ")))

    print(number_to_roman(input_num))

