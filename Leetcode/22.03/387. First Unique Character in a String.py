class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = {}
        for cha in s:
            cnt[cha] = cnt.get(cha, 0) + 1
        for i, cha in enumerate(s):
            if cnt[cha] == 1:
                return i
        return -1