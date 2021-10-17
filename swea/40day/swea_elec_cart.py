def dfs(res, flag, dep):
    global min_sum
    if res > min_sum:
        return
    if dep == N - 1:
        min_sum = min(min_sum, res + arr[flag][0])
        return
    for i in range(N):
        if check[i] == 0:
            check[i] = 1
            dfs(res + arr[flag][i], i, dep + 1)
            check[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    check[0] = 1
    min_sum = int(21e8)
    dfs(0, 0, 0)
    print("#{} {}".format(tc, min_sum))
