
# bloom 응용
from collections import deque
dy = [-1,1,0,0]
dx = [0,0,-1,1]
def bfs(sy,sx):
    visited = [[0 for _ in range(5)] for _ in range(3)]
    queue = deque()
    queue.append((sy,sx,1))
    visited[sy][sx] = 1
    ans = 0
    while queue :
        now = queue.popleft() # [0]:y  [1]:x  // [2]: level
        ans = now[2]
        for t in range(4):
            ny = now[0] + dy[t]
            nx = now[1] + dx[t]
            if ny < 0 or nx < 0 or ny >= 3 or nx >= 5: continue
            if visited[ny][nx] == 1 : continue
            visited[ny][nx] = 1
            queue.append((ny,nx,now[2]+1))

    return ans

ret = bfs(0,0)
print(ret)

