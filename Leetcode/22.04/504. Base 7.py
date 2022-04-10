class Solution:
    def convertToBase7(self, num: int) -> str:
        neg_flag = False
        res = ""
        if num < 0:
            num = -num
            neg_flag = True
        while num >= 7:
            res += str(num % 7)
            num = num // 7
        res += str(num)
        if neg_flag:
            return "-" + res[::-1]
        return res[::-1]