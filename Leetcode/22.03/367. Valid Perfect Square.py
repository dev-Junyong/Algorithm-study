class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        end = num // 2
        
        while (start + 1) < end:
            mid = start + (end - start) // 2
            if (mid * mid) < num:
                start = mid
            elif (mid * mid) > num:
                end = mid
            else:
                return True
        
        if (start * start) != num and (end * end) != num:
            return False
        
        return True