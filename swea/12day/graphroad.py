def dfs(now):
    for next in range(1, V + 1):
        if adj[now][next] == 0:
            continue
        if visited[next] == 1:
            continue
        visited[next] = 1
        dfs(next)


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    for i in range(E):
        a, b = map(int, input().split())
        adj[a][b] = 1
    S, G = map(int, input().split())
    visited = [0 for _ in range(V + 1)]
    visited[S] = 1
    dfs(S)
    if visited[G] == 1:
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))
