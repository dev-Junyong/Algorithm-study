class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s).values()
        res = 0
        for x in cnt:
            if x // 2 > 0:
                res += x // 2 * 2
        if res == len(s):
            return res
        else:
            return res + 1