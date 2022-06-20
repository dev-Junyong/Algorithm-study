n = int(input())
t_lst = list(map(int, input().split()))
t_lst.sort()

total = 0
wait = 0

for t in t_lst:
    wait += t
    total += wait
print(total)
