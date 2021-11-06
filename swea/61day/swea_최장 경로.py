T = int(input())


def dfs(now, cnt):
    global max_path
    max_path = max(max_path, cnt)

    for next in adj[now]:
        if visited[next] == 1:
            continue  
        visited[next] = 1 
        dfs(next, cnt + 1)
        visited[next] = 0  


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    adj = [
        [] for _ in range(N + 1) 
    ]
    de = - 1
    for _ in range(M):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    max_path = 0
    visited = [0] * (N + 1)
    for i in range(1, N + 1):
        visited[i] = 1  
        dfs(i, 1)
        visited[i] = 0  
    print("#{} {}".format(tc, max_path))
