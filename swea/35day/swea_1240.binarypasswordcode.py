T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data_tmp = [str(input()) for _ in range(N)]
    code = ['0001101', '0011001', '0010011', '0111101', '0100011',
            '0110001', '0101111', '0111011', '0110111', '0001011']

    flag = False
    for i in range(M - 7):
        if flag:
            break
        for j in range(N):
            if flag:
                break
            tmp = data_tmp[j][i:i + 7]
            if tmp != '0000000':
                lst = []
                for k in range(len(code)):
                    if tmp == code[k]:
                        for l in range(8):
                            tmp = data_tmp[j][i + (l * 7): i + (l * 7) + 7]
                            for m in range(len(code)):
                                if tmp == code[m]:
                                    lst.append(m)
                        if len(lst) == 8:
                            flag = True
                            break

    if ((lst[0] + lst[2] + lst[4] + lst[6]) * 3 + lst[1] + lst[3] + lst[5] + lst[7]) % 10 == 0:
        print('#{} {}'.format(tc, sum(lst)))
    else:
        print('#{} {}'.format(tc, 0))


