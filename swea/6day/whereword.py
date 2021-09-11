
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    map_arr = []
    for _ in range(N):
        map_arr.append(list(map(int, input().split())))

    fit_num = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if map_arr[i][j] == 0:
                if cnt == K:
                    fit_num += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == K:
            fit_num += 1

    for j in range(N):
        cnt = 0
        for i in range(N):
            if map_arr[i][j] == 0:
                if cnt == K:
                    fit_num += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == K:
            fit_num += 1

    print("#{} {}".format(tc, fit_num))
