
for tc in range(1, 10+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    cnt = 0

    for i in range(1 << N):
        total_sum = 0
        for j in range(N+1):
            if i & (1 << j):
                total_sum += num_list[j]
        if total_sum == 0:
            cnt += 1

    print("#{} {}".format(tc, cnt))
