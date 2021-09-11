
T = int(input())

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    cnt = 0

    for i in range(1 << len(num_list)):
        sum1 = 0
        num_cnt = 0
        for j in range(12):
            if i & (1 << j):
                sum1 += num_list[j]
                num_cnt += 1
        if sum1 == k and num_cnt == n:
            cnt += 1
    print("#{} {}".format(tc, cnt))

