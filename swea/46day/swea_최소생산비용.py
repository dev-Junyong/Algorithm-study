def dfs(level, total):  # 행, 현재 타임 합
    global res
    if level == N:
        res = min(total, res)
        return
    if total >= res:
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(level + 1, total + arr[level][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = int(21e8)
    visited = [0] * N
    dfs(0, 0)
    print("#{} {}".format(tc, res))
