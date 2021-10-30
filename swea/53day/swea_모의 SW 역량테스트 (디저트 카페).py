def func(r, c, k, cnt):
    global max_num, si, sj
    if k == 3 and si == r and sj == c:
        if max_num < cnt:
            max_num = cnt
    if k == 2 and max_num > (cnt * 2):
        return
    if not check(r, c):
        return
    if arr[r][c] in des:
        return
    else:
        des.append(arr[r][c])
        if k == 0 or k == 1:
            func(r + dr[k], c + dc[k], k, cnt + 1)
            func(r + dr[k + 1], c + dc[k + 1], k + 1, cnt + 1)
        elif k == 2:
            if r + c != si + sj:
                func(r + dr[k], c + dc[k], k, cnt + 1)
            else:
                func(r + dr[k + 1], c + dc[k + 1], k + 1, cnt + 1)
        else:
            func(r + dr[k], c + dc[k], k, cnt + 1)
        des.remove(arr[r][c])


def check(a, b):
    return 0 <= a < n and 0 <= b < n


dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    des = []
    max_num = -1
    for i in range(n):
        for j in range(n):
            si, sj = i, j
            des.append(arr[i][j])
            func(i + 1, j + 1, 0, 1)
            des.remove(arr[i][j])

    print("#{} {}".format(tc, max_num))


