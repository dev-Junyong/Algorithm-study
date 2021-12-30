def check(arr, row_s, row_e, col_s, col_e):
    n = len(arr)
    res = 1

    for r in range(row_s, row_e+1):
        cnt = 1
        for c in range(1, n):
            if arr[r][c-1] == arr[r][c]:
                cnt += 1
            else:
                cnt = 1
            if cnt > res:
                res = cnt
    for r in range(col_s, col_e+1):
        cnt = 1
        for c in range(1, n):
            if arr[c-1][r] == arr[c][r]:
                cnt += 1
            else:
                cnt = 1
            if cnt > res:
                res = cnt
    return res


n = int(input())
arr = [list(input()) for _ in range(n)]
res = 0

for i in range(n):
    for j in range(n):
        if j < n-1:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            temp = check(arr, i, i, j, j+1)
            if temp > res:
                res = temp
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        if i < n-1:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            temp = check(arr, i, i+1, j, j)
            if temp > res:
                res = temp
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(res)
