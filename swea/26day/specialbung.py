T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    time_lst = list(map(int, input().split()))

    for i in range(len(time_lst)-1, 0, -1):
        for j in range(i):
            if time_lst[j] > time_lst[j+1]:
                time_lst[j], time_lst[j+1] = time_lst[j+1], time_lst[j]

    cnt = 0
    flag = 1
    for r in time_lst:
        bread = (r//M)*K
        if bread - cnt <= 0:
            flag = 0
            break
        else:
            cnt += 1
    if flag == 1:
        print("#{} Possible".format(tc))
    else:
        print("#{} Impossible".format(tc))

