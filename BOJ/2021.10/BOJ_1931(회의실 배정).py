N = int(input())
time_lst = []

for _ in range(N):
    st_time, en_time = map(int, input().split())
    time_lst.append([st_time, en_time])

time_lst = sorted(time_lst, key=lambda x: x[0])
time_lst = sorted(time_lst, key=lambda x: x[1])

flag_last = 0
tmp = 0
for i, j in time_lst:
    if i >= flag_last:
        tmp += 1
        flag_last = j

print(tmp)
