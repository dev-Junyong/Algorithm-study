class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        len_words = len(wordsDict)
        index1 = len_words
        index2 = len_words
        res = len_words
        
        for i in range(len_words):
            if wordsDict[i] == word1:
                index1 = i
                res = min(res, abs(index1 - index2))
            elif wordsDict[i] == word2:
                index2 = i
                res = min(res, abs(index1 - index2))
        return res