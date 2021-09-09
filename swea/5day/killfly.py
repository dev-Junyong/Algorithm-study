T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr_list = [list(map(int, input().split())) for _ in range(N)]

    max_num = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            now_num = 0
            for k in range(M):
                for p in range(M):
                    now_num += arr_list[j + p][i + k]
            if now_num > max_num:
                max_num = now_num
    print("#{} {}".format(tc, max_num))
