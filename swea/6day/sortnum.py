T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    for j in range(n):
        k = n-j
        for i in range(1, k):
            if lst[i-1] >= lst[i]:
                lst[i-1], lst[i] = lst[i], lst[i-1]

    print("#{}".format(tc), *lst)

