def nqueen(level):
    global res
    if level == N:
        res += 1
        return
    else:
        for i in range(N):
            s, e = level + i, level - i + N - 1
            if col[i] or lst1[s] or lst2[e]:
                continue
            col[i], lst1[s], lst2[e] = 1, 1, 1
            nqueen(level + 1)
            col[i], lst1[s], lst2[e] = 0, 0, 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    col = [0] * N
    lst1 = [0] * (N * 2 - 1)
    lst2 = [0] * (N * 2 - 1)
    res = 0
    nqueen(0)
    print('#{} {}'.format(tc, res))
