class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        index = [i for i in range(len(s)) if s[i] in vowels]
        half, count = len(index) // 2, len(index) - 1
        s_lst = list(s)
        for i in range(half):
            s_lst[index[i]], s_lst[index[count - i]] = s_lst[index[count - i]], s_lst[index[i]]
        return ''.join(s_lst)