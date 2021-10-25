
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    res = []
    for i in money:
        res.append(N // i)
        N %= i
    print('#{}'.format(tc))
    print(*res)
