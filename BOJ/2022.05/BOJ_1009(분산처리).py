t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    res = pow(a, b, 10)

    if not res:
        print(res + 10)
    else:
        print(res)