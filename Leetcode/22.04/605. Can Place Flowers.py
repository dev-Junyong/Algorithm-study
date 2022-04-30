class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        checked = [0] + flowerbed + [0]
        len_flo = len(checked)
        chk = 0
        
        for i in range(1, len_flo - 1):
            if checked[i] == checked[i - 1] == checked[i + 1] == 0:
                chk += 1
                checked[i] = 1
                
        return chk >= n