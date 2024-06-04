"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        pass
        
    def number_to_thai(number):
            units = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
            tens = ["", "สิบ", "ยี่สิบ", "สามสิบ", "สี่สิบ", "ห้าสิบ", "หกสิบ", "เจ็ดสิบ", "แปดสิบ", "เก้าสิบ"]
            hundreds = ["", "หนึ่งร้อย", "สองร้อย", "สามร้อย", "สี่ร้อย", "ห้าร้อย", "หกร้อย", "เจ็ดร้อย", "แปดร้อย", "เก้าร้อย"]
            
            if number == 0:
                return "ศูนย์"
            if number < 0:
                return "number can not less than 0"
            
            def convert_to_text(n):
                if n < 10:
                    return units[n]
                elif n < 20:
                    if n == 10:
                        return "สิบ"
                    elif n == 11:
                        return "สิบเอ็ด"
                    else:
                        return "สิบ" + units[n % 10]
                    
                elif n < 100:
                    return tens[n // 10] + (units[n % 10] if n % 10 != 0 else "")
                elif n < 1000:
                    return hundreds[n // 100] + (convert_to_text(n % 100) if n % 100 != 0 else "")
             

            return convert_to_text(number)
        
    input_num = (int(input("Enter a number : ")))

    print(number_to_thai(input_num))
                                    
