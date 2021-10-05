T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'A':
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0 <= ny < n and 0 <= nx < n:
                        if arr[ny][nx] == 'H':
                            arr[ny][nx] = 'X'
            elif arr[i][j] == 'B':
                for k in range(4):
                    for p in range(1, 3):
                        ny = i + dy[k]*p
                        nx = j + dx[k]*p
                        if 0 <= ny < n and 0 <= nx < n:
                            if arr[ny][nx] == 'H':
                                arr[ny][nx] = 'X'
            elif arr[i][j] == 'C':
                for k in range(4):
                    for p in range(1, 4):
                        ny = i + dy[k]*p
                        nx = j + dx[k]*p
                        if 0 <= ny < n and 0 <= nx < n:
                            if arr[ny][nx] == 'H':
                                arr[ny][nx] = 'X'

    cnt = 0
    for a in range(n):
        for b in range(n):
            if arr[a][b] == 'H':
                cnt += 1

    print(f'#{tc} {cnt}')

