class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        
        for i in range(left, right+1):
            strnum = str(i)
            flag = 0
            for stn in strnum:
                if int(stn) == 0:
                    flag = 1
                    continue
                if i % int(stn) !=0:
                    flag = 1
            if flag == 0 :
                res.append(i)
                
        return res