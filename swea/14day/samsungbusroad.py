
T = int(input())

for tc in range(1, T+1):
    n = int(input())

    chk_list = [0]*5001
    for i in range(n):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            chk_list[j] += 1

    p = int(input())

    result = []
    for k in range(p):
        c = int(input())
        result.append(chk_list[c])

    print("#{}".format(tc), end=' ')
    print(*result)
