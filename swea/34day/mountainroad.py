def dfs(r, c, cut, road):
    global res
    if res < road + 1:
        res = road + 1

    visited[r][c] = 1  
    for i in range(4):
        ny = r + dy[i]
        nx = c + dx[i]

        if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
            if MAP[r][c] > MAP[ny][nx]:
                dfs(ny, nx, cut, road + 1)
            elif cut == 0 and MAP[r][c] > MAP[ny][nx] - K:
                tmp = MAP[ny][nx]
                MAP[ny][nx] = MAP[r][c] - 1  
                dfs(ny, nx, 1, road + 1)
                MAP[ny][nx] = tmp  
    visited[r][c] = 0  


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dy = [-1, 1, 0, 0]  
    dx = [0, 0, -1, 1]

    start = 0
    for r in range(N):
        for c in range(N):
            if start < MAP[r][c]:
                start = MAP[r][c]

    res = 0
    for y in range(N):
        for x in range(N):
            if MAP[y][x] == start:
                dfs(y, x, 0, 0)

    print('#{} {}'.format(tc, res))
