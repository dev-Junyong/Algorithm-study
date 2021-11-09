def search(k):
    global cnt, visited
    q = []
    q.append(k)
    visited[k] = 1
    while q:
        s = q.pop(0)
        for k in range(N + 1):
            if arr[s][k] == 1 and visited[k] == 0:
                q.append(k)
                visited[k] = 1
    return visited


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for m in range(M):
        s, e = map(int, input().split())
        arr[s][e] = 1
        arr[e][s] = 1
    cnt = 0
    for i in range(1, N + 1):
        if visited[i] == 0:
            search(i)
            cnt += 1
    print('#{} {}'.format(tc, cnt))


