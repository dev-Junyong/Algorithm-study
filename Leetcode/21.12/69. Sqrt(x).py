class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = int(21e8)
        while True:
            mid = left + (right - left) / 2
            if int(mid) > x / int(mid):
                right = int(mid) - 1
            else:
                if int(mid) + 1 > x / (int(mid) + 1):
                    return int(mid)
                left = int(mid) + 1