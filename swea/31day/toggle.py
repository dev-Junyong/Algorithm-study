
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    for k in range(1, m+1):
        for r in range(n):
            for c in range(n):
                if m % k == 0:
                    if arr[r][c] == 0:
                        arr[r][c] = 1
                    else:
                        arr[r][c] = 0
                elif (r+1+c+1) == k or (r+1+c+1) % k == 0:
                    if arr[r][c] == 0:
                        arr[r][c] = 1
                    else:
                        arr[r][c] = 0

    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1

    print("#{} {}".format(tc, cnt))
