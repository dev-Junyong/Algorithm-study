
T = int(input())
for tc in range(1, T + 1):
    num_2 = list(input())
    num_3 = list(input())
    lst2 = []
    lst3 = []
    res = 0
    for i in range(len(num_2)):
        if num_2[i] == '0':
            num_2[i] = '1'
            lst2.append(int("".join(num_2), 2))
            num_2[i] = '0'
        else:
            num_2[i] = '0'
            lst2.append(int("".join(num_2), 2))
            num_2[i] = '1'
    for j in range(len(num_3)):
        if num_3[j] == '0':
            num_3[j] = '1'
            lst3.append(int("".join(num_3), 3))
            num_3[j] = '2'
            lst3.append(int("".join(num_3), 3))
            num_3[j] = '0'
        elif num_3[j] == '1':
            num_3[j] = '0'
            lst3.append(int("".join(num_3), 3))
            num_3[j] = '2'
            lst3.append(int("".join(num_3), 3))
            num_3[j] = '1'
        else:
            num_3[j] = '0'
            lst3.append(int("".join(num_3), 3))
            num_3[j] = '1'
            lst3.append(int("".join(num_3), 3))
            num_3[j] = '2'
    for k in lst2:
        if k in lst3:
            res = k
            break
    print('#{} {}'.format(tc, res))
