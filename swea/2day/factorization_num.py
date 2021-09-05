
T = int(input())

for tc in range(1, T+1):
    result = [0]*5
    N = int(input())

    while N > 1:
        if N % 2 == 0:
            N = N // 2
            result[0] += 1
        if N % 3 == 0:
            N = N // 3
            result[1] += 1
        if N % 5 == 0:
            N = N // 5
            result[2] += 1
        if N % 7 == 0:
            N = N // 7
            result[3] += 1
        if N % 11 == 0:
            N = N // 11
            result[4] += 1

    print("#{} ".format(tc), end='')
    print(*result)
