class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        start = 0
        mid = k
        end = 2 * k
        res = ''
        while len(res) < len(s):
            res += s[start:mid][::-1] + s[mid:end]
            start = start + 2 * k
            mid = mid + 2 * k
            end = end + 2 * k
        return res