class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_lst = list(s)
        t_lst = list(t)
        s_lst.sort()
        t_lst.sort()
        for i in range(len(s_lst)):
            if s_lst[i] != t_lst[i]:
                return t_lst[i]
        return t_lst[-1]