N, M = map(int, input().split())
arr = [input() for _ in range(N)]
res = []

for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        temp = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if temp % 2 == 0:
                    if arr[k][l] != 'W':
                        cnt += 1
                else:
                    if arr[k][l] != 'B':
                        cnt += 1
                if l != j+7:
                    temp += 1

        res.append(min(cnt, 64-cnt))
print(min(res))
