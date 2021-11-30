import sys

c = int(sys.stdin.readline())
for _ in range(c):
    lst = list(map(int, sys.stdin.readline().split()))
    n = lst[0]
    total = 0
    for i in range(1, len(lst)):
        total += lst[i]
    avg_num = total / n
    cnt = 0
    for j in range(1, len(lst)):
        if lst[j] > avg_num:
            cnt += 1
    res = (cnt / n) * 100
    print("{:.3f}%".format(res))
