
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = [list(map(int, input().split())) for _ in range(N)]

    max_sum = int(-21e8)  # 최대값, 매우 작은 수로
    for i in range(N-M+1):  # 파리채 범위 생각해서 범위 지정
        for j in range(N-M+1):
            tmp_sum = 0  # 임시 합
            for a in range(M):  # 파리채 합 시작
                for b in range(M):
                    tmp_sum += num_list[i+a][j+b]
            if max_sum < tmp_sum:
                max_sum = tmp_sum

    print("#{} {}".format(tc, max_sum))

