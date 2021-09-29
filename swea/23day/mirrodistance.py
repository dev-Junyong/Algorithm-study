from collections import deque

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    MAP = [list(map(int, input())) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]

    flag = 0
    for i in range(n):
        for j in range(n):
            if MAP[i][j] == 2:
                start_i = i
                start_j = j
    i, j = start_i, start_j
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    dr = [-1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    flag = 0
    while q:
        i, j = q.popleft()
        if MAP[i][j] == 3:
            flag = 1
            break

        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]

            if MAP[nr][nc] == 1 or visited[nr][nc] == 0:
                continue
            q.append((nr, nc))
            visited[nr][nc] = visited[i][j] + 1

    if flag == 1:
        print("#{} {}".format(tc, visited[i][j]-1))
    else:
        print("#{} 0".format(tc))

