
# 대각선 파리채 계산
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = [list(map(int, input().split())) for _ in range(N)]

    max_sum = int(-21e8)  # 최대값, 매우 작은 수로
    for i in range(N-M+1):  # 파리채 범위 생각해서 범위 지정
        for j in range(N-M+1):
            tmp_sum1 = 0  # 임시 합
            tmp_sum2 = 0
            tmp_total = 0
            tmp_dub = 0
            if M <= 2:
                for a in range(M):  # 파리채 합 시작
                    for b in range(M):
                        tmp_sum1 += num_list[i + a][j + b]
                tmp_total = tmp_sum1
            if M > 2 and M % 2 == 0:
                for a in range(M):  # 파리채 합 시작
                    tmp_sum1 += num_list[i+a][j+a]
                    tmp_sum2 += num_list[i+a][j+M-1-a]
                tmp_total = tmp_sum1 + tmp_sum2
            if M > 2 and M % 2 == 1:
                tmp_dub += num_list[(M // 2)+i][(M // 2)+j]
                for a in range(M):  # 파리채 합 시작
                    tmp_sum1 += num_list[i+a][j+a]
                    tmp_sum2 += num_list[i+a][j+M-1-a]

                tmp_total = tmp_sum1 + tmp_sum2 - tmp_dub

            if max_sum < tmp_total:
                max_sum = tmp_total

    print("#{} {}".format(tc, max_sum))
