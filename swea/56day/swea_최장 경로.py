def dfs(idx, a):
    global res
    if a > res:
        res = a
    for p in range(1, n + 1):
        if arr[idx][p] and visited[p] == 0:
            visited[p] = 1
            dfs(p, a + 1)
            visited[p] = 0


T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    visited = [0] * (n + 1)
    for i in range(m):
        r, c = map(int, input().split())
        arr[r][c] = 1
        arr[c][r] = 1
    res = 0
    for j in range(1, n + 1):
        visited[j] = 1
        dfs(j, 1)
        visited[j] = 0
    print('#{} {}'.format(tc, res))
