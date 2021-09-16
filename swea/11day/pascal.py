
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = []

    for i in range(1, N+1):
        lst.append([1]*i)

    for j in range(N):
        if j >= 2:
            for k in range(1, len(lst[j])-1):
                lst[j][k] = lst[j-1][k] + lst[j-1][k-1]

    print("#{}".format(tc))

    for a in range(N):
        print(*lst[a])
