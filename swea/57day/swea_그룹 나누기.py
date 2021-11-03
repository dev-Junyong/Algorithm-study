def Find(k):
    if parent[k] == k:
        return k
    parent[k] = Find(parent[k])
    return parent[k]


def Union(a, b):
    global res
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        res -= 1
        parent[pb] = pa
    return


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = [i for i in range(N + 1)]
    res = N
    for j in range(M):
        a = arr[j * 2]
        b = arr[j * 2 + 1]
        Union(a, b)
    print('#{} {}'.format(tc, res))
