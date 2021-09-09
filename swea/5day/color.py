T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    box_arr = [[0 for i in range(10)] for j in range(10)]

    color_cnt = 0
    for a in range(n):
        row1, col1, row2, col2, color_num = map(int, input().split())
        for b in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                box_arr[b][c] += color_num
                if box_arr[b][c] == 3:
                    color_cnt += 1

    print("#{} {}".format(tc, color_cnt))
