class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        len_s = len(s)
        
        for i in range(len_s):
            s_chk = s[i]
            t_chk = t[i]
            if s_chk in map1:
                if t_chk != map1[s_chk]:
                    return False
            
            else:
                if t_chk in map2:
                    return False
                else:
                    map1[s_chk] = t_chk
                    map2[t_chk] = ""
        return True