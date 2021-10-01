import sys

N, M = map(int, sys.stdin.readline().split())

res = []


def func(dep):
    if dep == M:
        print(*res)
    else:
        for i in range(1, N + 1):
            if i not in res:
                res.append(i)
                func(dep + 1)
                res.pop()


func(0)
