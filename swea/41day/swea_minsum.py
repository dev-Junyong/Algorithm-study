def min_sum(r, c, res):
    global min_num
    res += tmp[r][c]
    # if res > tmp:
    #     return
    # if r >= N or c >= N:
    #     return
    if r == N - 1 and c == N - 1:
        if min_num > res:
            min_num = res
        return
    if 0 <= r + 1 < N:
        min_sum(r + 1, c, res)
    if 0 <= c + 1 < N:
        min_sum(r, c + 1, res)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tmp = list()
    for i in range(N):
        tmp.append(list(map(int, input().split())))
    min_num = int(21e8)

    min_sum(0, 0, 0)
    print("#{} {}".format(tc, min_num))
