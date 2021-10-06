
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [[0 for _ in range(10)] for _ in range(10)]

    for i in range(n):
        r1, c1, r2, c2 = map(int, input().split())

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                arr[r][c] = 1

    cnt = 0
    for k in range(10):
        for p in range(10):
            if arr[k][p] == 1:
                cnt += 1
    print("#{} {}".format(tc, cnt))
