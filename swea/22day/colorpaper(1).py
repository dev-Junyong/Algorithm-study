n = int(input())
MAP = [[0 for _ in range(101)] for _ in range(101)]
ans = 0
for i in range(n):
    left1, bottom1 = map(int, input().split())
    for j in range(left1, left1+10):
        for k in range(bottom1, bottom1+10):
            MAP[j][k] = 1

for r in range(101):
    for c in range(101):
        if MAP[r][c] == 1:
            ans += 1
        else:
            continue
print(ans)
