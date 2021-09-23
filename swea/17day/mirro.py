
def dfs(r, c):
    global result
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    if MAP[r][c] == 3:
        result = 1
        return
    for k in range(4):
        ny = r + dy[k]
        nx = c + dx[k]
        if ny < 0 or nx < 0 or N <= ny or N <= nx:
            continue
        if visited[ny][nx] == 1:
            continue
        if MAP[ny][nx] == 1:
            continue
        visited[ny][nx] = 1
        dfs(ny, nx)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().rstrip())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 2:
                visited[i][j] = 1
                dfs(i, j)

    print("#{} {}".format(tc, result))
