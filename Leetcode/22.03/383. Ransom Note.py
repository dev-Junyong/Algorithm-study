class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        word_map = {}
        for word in magazine:
            word_map[word] = word_map.get(word, 0) + 1
        for word in ransomNote:
            word_map[word] = word_map.get(word, 0) - 1
            if word_map[word] < 0:
                return False
        return True