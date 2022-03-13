class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        len_word = len(word)
        cnt = loc = 0
        for i in abbr:
            if i.isdigit():
                if i == '0' and cnt == 0:
                    return False
                cnt = cnt * 10 + int(i)
            else:
                loc += cnt
                cnt = 0
                if loc >= len_word or word[loc] != i:
                    return False
                loc += 1
        return loc + cnt == len_word