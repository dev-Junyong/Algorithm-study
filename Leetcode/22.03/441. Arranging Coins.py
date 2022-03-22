class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        k = 1
        while n > 0:
            if n - k > 0:
                n -= k
                k += 1
            elif n == k:
                return k
            else:
                return k-1