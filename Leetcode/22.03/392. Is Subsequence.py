class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        flag = 0
        for cha in t:
            if cha == s[flag]:
                flag += 1
            if flag == len(s):
                break
        return flag == len(s)