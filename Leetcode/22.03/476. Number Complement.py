class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        bit = num
        flag = 1
        while bit:
            num ^= flag 
            bit >>= 1 
            flag <<= 1 
        return num