class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dict = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        res = ''
        for i in num:
            if i not in dict:
                return False
            res += dict[i]
        return res[::-1] == num