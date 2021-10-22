def b_search(start, end, flag, i):
    global cnt
    while start <= end:
        mid = (start + end) // 2
        if i >= N_lst[mid]:
            if i == N_lst[mid]:
                cnt += 1
                break
            start = mid + 1
            if flag == 1:
                break
            flag = 1
        elif i < N_lst[mid]:
            end = mid - 1
            if flag == -1:
                break
            flag = -1
    return


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    N_lst = list(map(int, input().split()))
    N_lst = sorted(N_lst)
    M_lst = list(map(int, input().split()))
    cnt = 0
    for i in M_lst:
        start = 0
        end = N - 1
        flag = 0
        b_search(start, end, flag, i)

    print('#{} {}'.format(tc, cnt))
