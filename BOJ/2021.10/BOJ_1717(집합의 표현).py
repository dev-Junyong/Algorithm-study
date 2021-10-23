import sys
sys.setrecursionlimit(100000)

def find(k):
    if k == parent[k]:
        return k
    parent[k] = find(parent[k])
    return parent[k]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, sys.stdin.readline().split())

parent = [i for i in range(N + 1)]

for _ in range(M):
    oper, a, b = map(int, sys.stdin.readline().split())
    if oper:
        findA = find(a)
        findB = find(b)
        if findA == findB:
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)
