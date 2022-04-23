class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        arr = [[0]*c for _ in range(r)]
        if row * col == r * c and row * col != 0:
            rows = 0
            cols = 0
            for i in range(row):
                for j in range(col):
                    arr[rows][cols] = mat[i][j]
                    cols += 1
                    if cols==c:
                        rows += 1
                        cols = 0
            return arr
        else:
            return mat