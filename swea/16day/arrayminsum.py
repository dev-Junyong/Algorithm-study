
def check(i):
    global min_num, max_sum
    if max_sum > min_num:
        return
    if i >= N:
        if max_sum < min_num:
            min_num = max_sum
            return

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            max_sum += MAP[i][j]
            check(i+1)
            max_sum -= MAP[i][j]
            visited[j] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    min_num = 21e8
    max_sum = 0
    check(0)
    print("#{} {}".format(tc, min_num))

