def check(row, col):
    if row < 0 or row == N:
        return False
    if col < 0 or col == N:
        return False
    if visited[arr[row][col]] == 1:
        return False
    return True


def start(k):
    if visited[k] == 1:
        return False
    for i in range(N):
        for j in range(N):
            if arr[i][j] == k:
                row, col = i, j
    return k, row, col


def bfs(row, col):
    global cnt
    if visited[len(visited) - 1] == 1:
        return
    for i in range(4):
        nr, nc = row + dy[i], col + dx[i]
        if check(nr, nc) and arr[nr][nc] == arr[row][col] + 1:
            visited[arr[nr][nc]] = 1
            cnt += 1
            bfs(nr, nc)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N + 1)
    flag = 1
    res = 1
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    for i in range(1, N * N + 1):
        if start(i):
            idx, row, col = start(i)
            cnt = 1
            bfs(row, col)
            if cnt > res:
                flag, res = i, cnt
    print("#{} {} {}".format(tc, flag, res))
