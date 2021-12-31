
N, L = map(int, input().split())

arr = [False] * 1001
for i in map(int, input().split()):
    arr[i] = True

res = 0
flag = 0

while flag < 1001:
    if arr[flag]:
        res += 1
        flag += L
    else:
        flag += 1

print(res)
