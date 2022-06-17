class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        nowColor = image[sr][sc]   

        def dfs(x, y):

            if 0 <= x < m and 0 <= y < n and image[x][y] == nowColor and image[x][y] != color:  
                image[x][y] = color
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y + 1)   
                dfs(x, y - 1)        

        dfs(sr, sc)

        return image