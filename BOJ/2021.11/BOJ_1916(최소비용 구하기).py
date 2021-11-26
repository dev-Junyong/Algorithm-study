# 시간 초과, 해결 못함
import sys
import heapq


def func(sc, idx):
    dist = [int(21e8) for _ in range(n + 1)]
    dist[idx] = 0
    queue = [(sc, idx)]
    while queue:
        tmp = heapq.heappop(queue)
        tmp_sc, tmp_idx = tmp[0], tmp[1]
        for r, c in arr[tmp_idx]:
            if dist[c] > tmp_sc + r:
                dist[c] = tmp_sc + r
                heapq.heappush(queue, (dist[c], c))
            else:
                continue
    return dist


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

arr = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, cost = map(int, sys.stdin.readline().split())
    arr[s].append((cost, e))

start, end = map(int, sys.stdin.readline().split())
res = func(0, start)
print(res[end])
