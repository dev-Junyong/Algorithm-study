
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]

    min_num = int(21e8)
    w_cnt = 0
    for r in range(n-2):
        for c in range(m):
            if arr[r][c] != 'W':
                w_cnt += 1
        b_cnt = 0
        for b in range(r+1, n-1):
            for c in range(m):
                if arr[b][c] != 'B':
                    b_cnt += 1
            r_cnt = 0
            for p in range(b+1, n):
                for c in range(m):
                    if arr[p][c] != 'R':
                        r_cnt += 1
            cnt_total = w_cnt + b_cnt + r_cnt

            if min_num > cnt_total:
                min_num = cnt_total

    print("#{} {}".format(tc, min_num))
