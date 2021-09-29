from collections import deque


def bfs(r, c):
    global n
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    while q:
        i, j = q.popleft()
        if MAP[i][j] == 3:
            return 1
        for k in range(4):
            nx = i + dy[k]
            ny = j + dx[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if MAP[ny][nx] == 1:
                continue
            if visited[ny][nx] == 1:
                continue
            q.append((ny, nx))
            visited[ny][nx] = 1
    return 0


for tc in range(1, 10 + 1):
    T = int(input())
    n = 16
    MAP = [list(map(int, input())) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]

    r, c = 0, 0
    for i in range(16):
        for j in range(16):
            if MAP[i][j] == 2:
                r = i
                c = j

    ans = bfs(r, c)

    print('#{} {}'.format(T, ans))
