class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        s_lst = list(s)
        n_lst = []
        res = 0
        
        for i in s_lst:
            n_lst.append(dict.get(i))
        
        for j in range(0, len(n_lst)):
            if j == len(n_lst)-1:
                res += n_lst[j]
            elif n_lst[j] >= n_lst[j+1]:
                res += n_lst[j]
            elif n_lst[j] < n_lst[j+1]:
                res -= n_lst[j]
        
        return res
        