class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack is None or needle is None:
            return -1
        if haystack == needle:
            return 0
        
        n_len = len(needle)
        
        for i in range(len(haystack) - n_len + 1):
            if haystack[i:i+n_len] == needle:
                return i
        return -1