"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        pass

    def count_trailing_zeros(n):
        factorial = 1

        if n < 0:
            return "number can not be negative"
        
        for i in range(2, n + 1):
            factorial *= i
        
        count = 0
        while factorial % 10 == 0:
            count += 1
            factorial //= 10
        
        return count



    n = int(input("Enter a number: "))

    result = count_trailing_zeros(n)
    
    print("Result : ", result)


