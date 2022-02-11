class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnt = collections.Counter(s)
        temp = 1
        for i in cnt:
            if cnt[i] % 2 != 0:
                temp -= 1
                if temp < 0:
                    return False
        return True