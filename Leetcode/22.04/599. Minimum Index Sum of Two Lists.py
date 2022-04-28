class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = float(21e8)
        res = []
        chk = {}
        
        for i in range(len(list1)):
            chk[list1[i]] = i
            
        for j in range(len(list2)):
            if list2[j] in chk:
                if j + chk[list2[j]] == min_sum:
                    res.append(list2[j])
                elif j + chk[list2[j]] < min_sum:
                    min_sum = j + chk[list2[j]]
                    res = [list2[j]]
        return res