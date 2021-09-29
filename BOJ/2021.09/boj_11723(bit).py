import sys

m = int(sys.stdin.readline())
res = 1 << 21
for _ in range(m):
    lst = sys.stdin.readline().split()
    tmp = lst[0]
    if len(lst) == 2:
        x = int(lst[1])

    if tmp == "add":
        res |= (1 << x)
    elif tmp == "remove":
        res &= ~(1 << x)
    elif tmp == "check":
        print(1) if res & 1 << x else print(0)
    elif tmp == "toggle":
        res ^= (1 << x)
    elif tmp == "all":
        res |= (1 << 22) - 1
    elif tmp == "empty":
        res &= 2 ** 21


