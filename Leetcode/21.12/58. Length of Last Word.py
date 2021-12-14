class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.split()
        len_new = 0
        len_new = len(new[-1])
        
        return len_new
        