def brick(arr, H, W, i, j, B):
    n = arr[i][j]
    arr[i][j] = 0
    B -= 1
    for k in range(4):
        y, x = i, j
        for _ in range(n - 1):
            y, x = y + dy[k], x + dx[k]
            if 0 <= y < H and 0 <= x < W:
                if arr[y][x]:
                    B = brick(arr, H, W, y, x, B)
            else:
                break
    return B


def total(arr, H, W):
    numbrick = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                numbrick += 1
    return numbrick


def backtrack(arr, H, W, N, K, B):
    global res
    if res == 0 or B == 0:
        res = 0
        return
    if K == N:
        res = min(res, B)
        return
    for j in range(W):
        carr = [g[:] for g in arr]
        backtrack(carr, H, W, N, K + 1, drop(carr, H, W, j, B))


def drop(arr, H, W, j, B):
    i = 0
    while i < H:
        if arr[i][j]:
            B = brick(arr, H, W, i, j, B)
            relocation(arr, W)
            break
        i += 1
    return B


def relocation(arr, W):
    arr2 = [list(z) for z in zip(*arr)]
    for i in range(W):
        arr2[i].sort(key=lambda t: 1 if t else 0)
    arr[:] = [list(z) for z in zip(*arr2)]


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

T = int(input())

for tc in range(1, T + 1):
    res = 10 * 12 * 15
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]

    backtrack(arr, H, W, N, 0, total(arr, H, W))
    print("#{} {}".format(tc, res))
