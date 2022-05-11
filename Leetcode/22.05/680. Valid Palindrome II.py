class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                temp_l = s[l + 1:r + 1]
                temp_r = s[l:r]
                return temp_l == temp_l[::-1] or temp_r == temp_r[::-1]
            l += 1
            r -= 1
        return True