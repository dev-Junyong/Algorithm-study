
n = int(input())
res = 0
for i in range(1, n+1):
    temp = list(map(int, str(i)))
    sum_num = i + sum(temp)
    if sum_num == n:
        res = i
        break

print(res)
