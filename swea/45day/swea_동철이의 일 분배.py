def func(m, tmp):
    global max_per
    if max_per >= tmp:
        return
    if N == m:
        if max_per < tmp:
            max_per = tmp
            return
    else:
        for k in range(m, N):
            work[m], work[k] = work[k], work[m]
            func(m + 1, (tmp * arr[m][work[m]]) / 100)
            work[m], work[k] = work[k], work[m]



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    work = [i for i in range(N)]
    max_per = 0
    func(0, 1)
    max_per = round(max_per * 100, 6)
    max_per = format(max_per, '.6f')
    print("#{} {}".format(tc, max_per))
