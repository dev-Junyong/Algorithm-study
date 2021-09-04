tc = int(input())

for test_ in range(1, tc + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans_num = 0

    for i in range(N):
        result = N-i-1
        for j in range(i+1, N):
            if lst[j] >= lst[i]:
                result -= 1

        if ans_num < result:
            ans_num = result
    print('#{} {}'.format(test_, ans_num))