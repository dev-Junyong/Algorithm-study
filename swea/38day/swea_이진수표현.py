T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    res = ''
    while M:
        tmp = M % 2
        res = str(tmp) + res
        M //= 2
    light = 'ON'

    print('#{}'.format(tc), end=' ')
    for i in range(len(res)-1, len(res)-1-N, -1):
        if i < 0:
            light = 'OFF'
            break
        elif res[i] == '0':
            light = 'OFF'
            break
    print('{}'.format(light))


