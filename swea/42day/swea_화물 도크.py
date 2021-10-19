T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    time_lst = [list(map(int, input().split())) for _ in range(N)]
    time_lst.sort(key=lambda x: x[1])
    res = 1
    flag = time_lst[0]
    for i in range(1, N):
        if time_lst[i][0] >= flag[1]:
            flag = time_lst[i]
            res += 1
    print('#{} {}'.format(tc, res))
