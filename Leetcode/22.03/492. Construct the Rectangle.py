class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        n = int(math.sqrt(area))
        
        while area % n != 0:
            n -= 1
            
        return [int(area/n),n]