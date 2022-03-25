class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ham_chk = 0
        while x or y:
            if (x & 1) != (y & 1):
                ham_chk += 1
            x = x >> 1
            y = y >> 1
        return ham_chk