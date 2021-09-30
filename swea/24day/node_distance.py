from collections import deque


def bfs(s):
    global v, e, g
    queue = deque()
    queue.append(s)
    visited[s] = 0

    while queue:
        now = queue.popleft()
        for next in range(1, v + 1):
            if adj[now][next] == 0 or visited[next]:
                continue
            visited[next] = visited[now] + 1
            queue.append(next)
    return visited[g]


T = int(input())

for tc in range(1, T + 1):
    v, e = map(int, input().split())
    MAP = [0] * (v + 1)
    visited = [0] * (v + 1)

    adj = [[0 for _ in range(v + 1)] for _ in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        adj[a][b] = 1
        adj[b][a] = 1

    s, g = map(int, input().split())

    ans = bfs(s)
    print("#{} {}".format(tc, ans))
