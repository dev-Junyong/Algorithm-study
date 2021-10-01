def func(level, start):
    if level == M:
        for i in range(M):
            print(path[i], end=' ')
        print()
        return
    for i in range(start, N + 1):
        path[level] = i
        func(level + 1, i)
        path[level] = 0


N, M = map(int, input().split())
path = [0] * 8
func(0, 1)