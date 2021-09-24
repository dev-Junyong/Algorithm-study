
def part_sum(i, sum1, cnt):
    global result
    if i >= 21:
        if sum1 == K and cnt == N:
            result += 1
        return
    if sum1 > K:
        return
    part_sum(i + 1, sum1 + i, cnt + 1)
    part_sum(i + 1, sum1, cnt)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = 0
    part_sum(1, 0, 0)
    print("#{} {}".format(tc, result))
