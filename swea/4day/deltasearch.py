for tc in range(1, 10 + 1):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    N = int(input())
    lst = [0 for _ in range(N)]
    for i in range(N):
        lst[i] = list(map(int, input().split()))
    sum1 = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if y < 0 or x < 0 or y >= N or x >= N:
                    continue
                if 0 <= y < N and 0 <= x < N:
                    sum1 += abs(lst[i][j] - lst[y][x])

    print("#{} {}".format(tc, sum1))

