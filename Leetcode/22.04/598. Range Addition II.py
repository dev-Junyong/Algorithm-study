class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_r = float(21e8)
        min_c = float(21e8)
        
        for op in ops:
            min_r = min(min_r, m, op[0])
            min_c = min(min_c, n, op[1])
            
        if min_r == float(21e8) or min_c == float(21e8):
            return m * n
        else:
            return min_r * min_c
        
