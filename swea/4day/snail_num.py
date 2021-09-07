T = int(input())
for tc in range(1, T + 1):

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    N = int(input())
    MAP = [[-1 for _ in range(N + 2)] for _ in range(N + 2)]
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            MAP[y][x] = 0

    x, y = 1, 1
    d = 0
    for n in range(1, N * N + 1):
        MAP[x][y] = n
        x += dx[d]
        y += dy[d]

        if MAP[x][y] != 0:
            x -= dx[d]
            y -= dy[d]
            d = (d + 1) % 4
            x += dx[d]
            y += dy[d]

    print('#{}'.format(tc))
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            print(MAP[y][x], end=' ')
            if x == N:
                print(' ')
