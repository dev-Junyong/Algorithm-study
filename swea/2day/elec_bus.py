T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    stat_list = list(map(int, input().split()))
    stations_list = [0]*(N+1)

    for num in stat_list:
        stations_list[num] += 1
    pre_stat = 0
    next_stat = 0
    cnt = 0
    next_stat += K

    while True:
        if next_stat >= N:
            break
        if stations_list[next_stat] == 1:
            cnt += 1
            pre_stat = next_stat
            next_stat += K
        else:
            next_stat -= 1
            if pre_stat == next_stat:
                cnt = 0
                break

    print("#{} {}".format(tc, cnt))

