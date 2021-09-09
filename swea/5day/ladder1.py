
for tc in range(1, 10+1):
    num = int(input())
    n = 100
    map_arr = [list(map(int, input().split())) for _ in range(n)]
    col = -100
    row = -100

    for i in range(n):
        if map_arr[n-1][i] == 2:
            col = i

    row = n-1

    while row > 0:
        if col > 0 and map_arr[row][col-1]:
            while col > 0 and map_arr[row][col-1]:
                col -= 1
            else:
                row -= 1
        elif 99 > col and map_arr[row][col+1]:
            while col < 99 and map_arr[row][col+1]:
                col += 1
            else:
                row -= 1
        else:
            row -= 1

    print("#{} {}".format(num, col))

