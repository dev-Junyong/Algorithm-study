for tc in range(1, 10 + 1):
    t = int(input())
    num_list = [list(map(int, input().split())) for _ in range(100)]

    a_sum = 0  # 대각선
    b_sum = 0  # 대각선
    max_num = int(-21e8)
    for i in range(100):
        r_sum = 0  # 가로
        c_sum = 0  # 세로
        a_sum += num_list[i][i]
        b_sum += num_list[i][99 - i]

        for j in range(100):
            r_sum += num_list[i][j]
            c_sum += num_list[j][i]
        if max_num < r_sum:
            max_num = r_sum
        if max_num < c_sum:
            max_num = c_sum
    if max_num < a_sum:
        max_num = a_sum
    if max_num < b_sum:
        max_num = b_sum

    print("#{} {}".format(t, max_num))

# 대각선으로 나눈 영역은 어떻게 되는지 생각해보기

