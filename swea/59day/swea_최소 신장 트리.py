def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


T = int(input())
for tc in range(1, T + 1):
    v, e = map(int, input().split())
    edge = []
    for _ in range(e):
        a, b, c = map(int, input().split())
        edge.append((c, a, b))
    edge.sort(key=lambda x: x[0])
    parent = list(range(v + 1))
    res = 0
    for w, s, e in edge:
        if find(s) != find(e):
            union(s, e)
            res += w
    print("#{} {}".format(tc, res))
