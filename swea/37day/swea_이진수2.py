
T = int(input())
for tc in range(1, T+1):
    N = float(input())
    tmp = 0
    res = ''
    cnt = 0
    while N:
        cnt += 1
        if cnt >= 13:
            res = 'overflow'
            break
        tmp = 2 ** (-cnt)
        if N >= tmp:
            N -= tmp
            res += '1'
        else:
            res += '0'

    print('#{} {}'.format(tc, res))
