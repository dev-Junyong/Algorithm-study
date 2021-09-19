
def check_chess(i, n):
    global ans
    if i == n:
        ans += 1
        return
    for j in range(n):
        if visited[j] == 0:
            visited[j] += 1
            check_chess(i+1, n)
            visited[j] -= 1
        else:
            continue


for tc in range(1, 10+1):
    N = int(input())
    visited = [0 for _ in range(N)]
    ans = 0
    check_chess(0, N)
    print("#{} {}".format(tc, ans))
