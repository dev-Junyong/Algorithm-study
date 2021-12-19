class Solution:
    dict = {}
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        else:
            return self.climbStairs1(n-1) + self.climbStairs1(n-2)
    
    def climbStairs1(self, n: int):
        if n not in self.dict.keys():
            self.dict[n] = self.climbStairs(n)
        return self.dict[n]
        