class Solution:
    def hammingWeight(self, n: int) -> int:
        temp = 0
        while n:
            n &= n - 1
            temp += 1
        return temp