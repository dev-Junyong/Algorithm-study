class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        temp = bin(n)[2:]
        
        for i in range(1, len(temp)):
            if temp[i - 1] == temp[i]:
                return False
        return True