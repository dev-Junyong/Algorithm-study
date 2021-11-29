import sys


def han(a):
    cnt = 0
    if a < 100:
        return a
    for i in range(100, a + 1):
        x = i // 100
        y = i % 100 // 10
        z = i % 10
        if x - y == y - z:
            cnt += 1
    return 99 + cnt


n = int(sys.stdin.readline())

res = han(n)
print(res)
