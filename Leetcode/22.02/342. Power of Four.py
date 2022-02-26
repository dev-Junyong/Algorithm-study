class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        temp = 0
        while n > 1 and temp == 0:
            temp = n % 4
            n = n / 4
            if n < 1 or temp != 0:
                return False
        return True