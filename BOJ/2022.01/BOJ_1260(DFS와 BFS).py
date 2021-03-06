
N, M, V = map(int, input().split())

graph = [[0]*(N + 1) for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = graph[e][s] = 1

visited = [0] * (N + 1)


def bfs(V):
    visited[V] = 0
    queue = [V]
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N + 1):
            if visited[i] == 1 and graph[V][i] == 1:
                queue.append(i)
                visited[i] = 0


def dfs(V):
    visited[V] = 1
    print(V, end=' ')

    for i in range(1, N + 1):
        if visited[i] == 0 and graph[V][i] == 1:
            dfs(i)


dfs(V)
print()
bfs(V)
