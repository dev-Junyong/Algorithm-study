
n = 19
arr = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 0, 1, 1]  # 우상, 우, 우하, 하
dx = [1, 1, 1, 0]
ans = 0
result = 0
a = 0
b = 0
for r in range(n):
    for c in range(n):
        if arr[r][c]:
            for k in range(4):
                ny = r + dy[k]
                nx = c + dx[k]
                ans = 1
                if ny < 0 or nx < 0 or ny >= n or nx >= n:
                    continue
                while 0 <= ny < n and 0 <= nx < n and arr[r][c] == arr[ny][nx]:
                    ans += 1
                    if ans == 5:
                        if 0 <= ny + dy[k] < n and 0 <= nx + dx[k] < n and arr[ny][nx] == arr[ny+dy[k]][nx+dx[k]]:
                            break
                        if 0 <= r - dy[k] < n and 0 <= c - dx[k] < n and arr[r][c] == arr[r-dy[k]][c-dx[k]]:
                            break
                        result = arr[r][c]
                        a = r + 1
                        b = c + 1
                        break
                    ny += dy[k]
                    nx += dx[k]

if not result:
    print('0')
else:
    print(result)
    print(a, b)

