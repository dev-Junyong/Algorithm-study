
from collections import deque

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    checked = [[0] * M for _ in range(N)]
    checked[0][0] = 1
    dq = deque()
    dq.append((0, 0, 1))
    while dq:
        r, c, res = dq.popleft()
        if r == N - 1 and c == M - 1:
            return res

        update_res = res + 1
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '1' and not checked[nr][nc]:
                checked[nr][nc] = 1
                dq.append((nr, nc, update_res))
            else:
                continue


print(bfs())
