# 보물섬

import sys
from collections import deque

dr = [-1, 1, 0, 0]  # 상하좌우
dc = [0, 0, -1, 1]


def bfs(r, c):
    q = deque([[r, c, 0]])
    visited = {(r, c)}
    while True:
        r, c, cnt = q.popleft()
        for k in range(4):
            ny = r + dr[k]
            nx = c + dc[k]
            if 0 <= ny < row and 0 <= nx < col and arr[ny][nx] == 'L' and (ny, nx) not in visited:
                q.append([ny, nx, cnt+1])
                visited.add((ny, nx))
        if len(q) == 0:
            return cnt


row, col = map(int, sys.stdin.readline().split())
arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(row)]

res = -1
for i in range(row):
    for j in range(col):
        if arr[i][j] == 'L':
            res = max(res, bfs(i, j))

print(res)
