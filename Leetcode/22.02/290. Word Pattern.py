class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1 = dict()
        d2 = dict()
        temp = s.split(" ")
        if len(pattern) != len(temp):
            return False
        for i in range(len(pattern)):
            n1 = d1.get(pattern[i])
            n2 = d2.get(temp[i])
            if n1 == None and n2 == None:
                d1[pattern[i]] = temp[i]
                d2[temp[i]] = pattern[i]
            elif n1 != temp[i] or n2 != pattern[i]:
                return False
        return True