
n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
coins.reverse()

res = 0
for coin in coins:
    res += k // coin
    k = k % coin

print(res)
