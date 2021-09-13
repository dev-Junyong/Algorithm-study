def is_garo(y, x, k):
    if x + k < N and MAP[y][x + k] == 1: 
        return 0
    if x - 1 >= 0 and MAP[y][x - 1] == 1: 
        return 0
    if x + k - 1 >= N: 
        return 0
    for i in range(k):
        if MAP[y][x + i] == 0:
            return 0
    return 1


def is_sero(y, x, k):
    if y + k < N and MAP[y + k][x] == 1: 
        return 0
    if y - 1 >= 0 and MAP[y - 1][x] == 1: 
        return 0
    if y + k - 1 >= N: 
        return 0
    for i in range(K):
        if MAP[y + i][x] == 0:
            return 0
    return 1


N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for y in range(N):
    for x in range(N):
        cnt += is_garo(y, x, K)
        cnt += is_sero(y, x, K)

print(cnt)
