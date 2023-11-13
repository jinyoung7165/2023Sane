#Integer To Roman
#2:I+I, 12:X+I+I, 27: X+X+V+I+I
#4/9 : IV/IX
#40/90 : XL/XC
#400/900 : CD/CM
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {1000:'M',900:'CM',500:'D',400:'CD',
                      100:'C',90:'XC',50:'L',40:'XL',
                      10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        result = ""
        while num > 0:
            for rom in roman_dict: #큰 단위부터 살핌
                if num - rom >= 0:
                    result += roman_dict[rom]
                    num -= rom
                    break #3000->MMM. 다시 1000으로 뺄 수 있는지 살펴야 함
        return result