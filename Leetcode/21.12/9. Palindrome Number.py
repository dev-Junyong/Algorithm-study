# 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        
        return x == x[::-1]

# 2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = None
        
        if x < 0:
            res = False
        else:
            tmp = x
            flag = 0
            while x:
                remain = x % 10
                x //= 10
                flag = flag * 10 + remain
            
            if flag == tmp:
                res = True
            else:
                res = False
        return res