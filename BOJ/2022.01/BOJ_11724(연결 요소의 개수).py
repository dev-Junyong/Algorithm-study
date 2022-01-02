import sys

input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[0] * N for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: x - 1, map(int, input().split()))
    adj[u][v] = adj[v][u] = 1

res = 0
checked = [0] * N


def dfs(now):
    for j in range(N):
        if adj[now][j] and not checked[j]:
            checked[j] = 1
            dfs(j)


for i in range(N):
    if not checked[i]:
        res += 1
        checked[i] = 1
        dfs(i)

print(res)

