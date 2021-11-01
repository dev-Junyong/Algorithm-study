# 시간 초과

def maxdivide(a, b):
    while a % b == 0:
        a = a / b
    return a


def isugly(num_i):
    num_i = maxdivide(num_i, 2)
    num_i = maxdivide(num_i, 3)
    num_i = maxdivide(num_i, 5)
    if num_i == 1:
        return 1
    else:
        return 0


def uglynum(input_num):
    i = 1
    cnt = 1

    while input_num > cnt:
        i += 1
        if isugly(i):
            cnt += 1
    return i


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    res = []
    print("#{} ".format(tc), end='')
    for i in lst:
        num = uglynum(i)
        res.append(str(num))

    print(" ".join(res))
