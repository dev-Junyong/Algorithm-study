class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [0] * (rowIndex + 1)
        for i in range(len(arr)):
            arr[i] = [0] * (i + 1)
        arr[0][0] = 1
        
        for j in range(rowIndex + 1):
            for k in range(j + 1):
                if k == 0 or k == j:
                    arr[j][k] = 1
                else:
                    arr[j][k] = arr[j - 1][k - 1] + arr[j - 1][k]
        
        return arr[rowIndex]