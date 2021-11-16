import sys
import heapq

v, e = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(v + 1)]
top = int(sys.stdin.readline())

for i in range(e):
    s, e, w = map(int, sys.stdin.readline().split())
    arr[s].append([w, e])

res = [int(21e8) for _ in range(v + 1)]
res[top] = 0

queue = []
heapq.heappush(queue, [0, top])

while queue:
    cnt, e = heapq.heappop(queue)
    if res[e] < cnt:
        continue
    for r, c in arr[e]:
        r += cnt
        if r < res[c]:
            res[c] = r
            heapq.heappush(queue, [r, c])
for k in range(1, v + 1):
    if res[k] != int(21e8):
        print(res[k])
    else:
        print("INF")
