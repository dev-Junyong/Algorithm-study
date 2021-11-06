import heapq


def func():
    global s, e
    queue = []
    heapq.heappush(queue, (0, 0))
    while queue:
        d, idx = heapq.heappop(queue)
        if visited[s]:
            continue
        visited[idx] = 1
        for s, e in arr[idx]:
            if dist[s] > d + e:
                dist[s] = d + e
                heapq.heappush(queue, (dist[s], s))
    return


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    dist = [0] + [int(21e8) for _ in range(N)]
    arr = [[] for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = list(map(int, input().split()))
        arr[s].append((e, w))
    func()
    res = dist[N]
    print('#{} {}'.format(tc, res))
