def dfs(level, total):
    global res
    if level == N:
        if total >= B:
            k = total - B
            if k < res:
                res = k
        return res
    else:
        dfs(level + 1, total + H_lst[level])
        dfs(level + 1, total)


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H_lst = list(map(int, input().split()))
    res = int(21e8)
    dfs(0, 0)
    print('#{} {}'.format(tc, res))
