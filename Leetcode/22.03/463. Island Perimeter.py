class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        n_row = len(grid)
        n_col = len(grid[0])
        for i in range(n_row):
            res += sum(grid[i]) * 4
            for j in range(n_col):
                if grid[i][j] == 1:
                    if i+1 < n_row and grid[i + 1][j] == 1:
                        res -= 2
                    if j+1 < n_col and grid[i][j + 1] == 1:
                        res -= 2
        return res