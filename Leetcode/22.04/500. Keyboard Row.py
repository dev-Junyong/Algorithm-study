class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        lst1 = ['q','w','e','r','t','y','u','i','o','p']
        lst2 = ['a','s','d','f','g','h','j','k','l']
        lst3 = ['z','x','c','v','b','n','m']

        res = []

        for word in words:
            flag1, flag2, flag3 = 0, 0, 0
            cnt = 0
            for i in word:
                if i in lst1:
                    flag1 = 1
                if i in lst2:
                    flag2 = 1
                if i in lst3:
                    flag3 = 1
            cnt = flag1 + flag2 + flag3
            if cnt == 1:
                res.append(word)

        return res