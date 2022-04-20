class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        rev_words = []
        
        for word in words:
            rev_words.append(word[::-1])
        
        return " ".join(rev_words)