for tc in range(1, 10 + 1):
    N = int(input())
    lst = []
    for i in range(100):
        bak_list = list(map(int, input().split()))
        lst.append(bak_list)

    max_num = 0
    for x in range(100):
        col_sum = 0
        row_sum = 0
        for y in range(100):
            col_sum += lst[x][y]
            row_sum += lst[y][x]
        max_num = max(col_sum, row_sum, max_num)

    col_sum = 0
    row_sum = 0
    for i in range(100):
        col_sum += lst[i][i]
        row_sum += lst[i][99 - i]
    max_num = max(col_sum, row_sum, max_num)

    print("#{} {}".format(tc, max_num))
