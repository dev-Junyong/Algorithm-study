
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    check_garo_list = []

    for i in range(N):
        check_garo = input()
        check_garo_list.append(check_garo)
        for j in range(N-M+1):
            last_idx = M+j
            if check_garo[j:last_idx] == check_garo[j:last_idx][::-1]:
                result = check_garo[j:last_idx]
    
    check_sero_list = []
    for k in range(N):
        check_sero = str()
        check_list = []
        for m in range(N):
            check_list.append(check_garo_list[m][k])
        check_sero = ''.join(check_list)
        check_sero_list.append(check_sero)
        for a in range(N-M+2):
            last_idx = M+a
            if check_sero[a:last_idx] == check_sero[a:last_idx][::-1]:
                result = check_sero[a:last_idx]

    print("#{} {}".format(tc, result))

