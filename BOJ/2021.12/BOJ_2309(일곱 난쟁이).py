lst = [int(input()) for _ in range(9)]

total = sum(lst)

for i in range(9):
    for j in range(i+1, 9):
        if total - (lst[i] + lst[j]) == 100:
            tmp1 = lst[i]
            tmp2 = lst[j]
            lst.remove(tmp1)
            lst.remove(tmp2)

            lst.sort()

            for k in range(len(lst)):
                print(lst[k])
            break

    if len(lst) < 9:
        break

