def dfs(row, col, cnt, total):
    if cnt > 7:
        return
    if cnt == 7:
        res.add(total)
        return
    for i in range(4):
        ny = row + dy[i]
        nx = col + dx[i]
        if 0 <= ny < 4 and 0 <= nx < 4:
            dfs(ny, nx, cnt + 1, total + arr[ny][nx])
        else:
            continue


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    arr = [list(input().split()) for _ in range(4)]
    res = set()
    for r in range(4):
        for c in range(4):
            dfs(r, c, 1, arr[r][c])

    print('#{} {}'.format(tc, len(res)))
