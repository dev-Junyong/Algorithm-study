from bisect import bisect_left, bisect_right
n = int(input())
n_lst = sorted(list(map(int, input().split())))

m = int(input())
m_lst = list(map(int, input().split()))
res = []
for i in m_lst:
    s = bisect_left(n_lst, i)
    e = bisect_right(n_lst, i)
    if e - s > 0:
        res.append(1)
    else:
        res.append(0)
print(*res)