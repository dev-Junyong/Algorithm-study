
# 테두리 파리채 계산
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = [list(map(int, input().split())) for _ in range(N)]

    max_sum = int(-21e8)  # 최대값, 매우 작은 수로
    de = -1
    for i in range(N-M+1):  # 파리채 범위 생각해서 범위 지정
        for j in range(N-M+1):
            tmp_sum1 = 0  # 가로 첫줄
            tmp_sum2 = 0  # 가로 마지막줄
            tmp_sum3 = 0  # 세로 왼쪽
            tmp_sum4 = 0  # 세로 오른쪽
            tmp_dub1 = 0  # 좌상
            tmp_dub2 = 0  # 우상
            tmp_dub3 = 0  # 좌하
            tmp_dub4 = 0  # 우하
            tmp_total = 0
            if M <= 2:
                for a in range(M):  # 파리채 합 시작
                    for b in range(M):
                        tmp_total += num_list[i + a][j + b]
            if 2 < M <= N:
                tmp_dub1 += num_list[i][j]
                tmp_dub2 += num_list[i][j+M-1]
                tmp_dub3 += num_list[i+M-1][j]
                tmp_dub4 += num_list[i+M-1][j+M-1]
                for a in range(M):  # 파리채 합 시작
                    for b in range(M):
                        tmp_sum1 += num_list[i][j+b]
                        tmp_sum2 += num_list[i+M-1][j+b]
                        tmp_sum3 += num_list[i+M-1][j]
                        tmp_sum4 += num_list[i-1+a][j+M-1]

                tmp_total = (tmp_sum1 + tmp_sum2 + tmp_sum3 + tmp_sum4) - (tmp_dub1 + tmp_dub2 + tmp_dub3 + tmp_dub4)

            if max_sum < tmp_total:
                max_sum = tmp_total

    print("#{} {}".format(tc, max_sum))
