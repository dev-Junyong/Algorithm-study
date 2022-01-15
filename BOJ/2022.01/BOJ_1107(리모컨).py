
N = int(input())
M = int(input())

if M > 0:
    broke_num = list(input().split())
else:
    broke_num = []

temp = []
for i in range(10):
    if str(i) not in broke_num:
        temp.append(str(i))

res = abs(N - 100)
for j in range(1000000):
    flag = 1
    for k in str(j):
        if k not in temp:
            flag = 0
            break
    if flag:
        res = min(res, abs(N - j) + len(str(j)))
print(res)

