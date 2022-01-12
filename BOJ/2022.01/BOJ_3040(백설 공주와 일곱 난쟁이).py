
num_lst = []
for _ in range(9):
    num_lst.append(int(input()))

total = sum(num_lst)
for i in range(9):
    total -= num_lst[i]
    for j in range(i+1, 9):
        total -= num_lst[j]
        if total == 100:
            num_lst.remove(num_lst[j])
            num_lst.remove(num_lst[i])
            break
        total += num_lst[j]
    else:
        total += num_lst[i]
        continue
    break
print(*num_lst, sep='\n')

