
T = int(input())
for tc in range(1, T+1):
    N, N_num = input().split()
    res = ''
    code = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for i in N_num:
        if '0' <= i <= '9':
            tmp = int(i)
        else:
            tmp = code[i]
        tmp_num = 8
        for j in range(4):
            if tmp & tmp_num:
                res += '1'
            else:
                res += '0'
            tmp_num >>= 1

    print('#{} {}'.format(tc, res))
