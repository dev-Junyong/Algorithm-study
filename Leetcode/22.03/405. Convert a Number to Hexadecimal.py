class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: 
            return "0" 
            
        code = "0123456789abcdef"
        res = ""

        if num < 0:
            num = (-num ^ 0xffffffff) + 1

        while num != 0:
            x = num & 0xf
            res = code[x] + res
            num = num >> 4

        return res