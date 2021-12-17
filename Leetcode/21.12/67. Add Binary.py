class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = int(a, 2)
        j = int(b, 2)
        
        return format(i+j, 'b')