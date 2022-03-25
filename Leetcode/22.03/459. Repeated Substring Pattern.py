class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        re_s = (s + s)[1:-1]
        return re_s.find(s) != -1