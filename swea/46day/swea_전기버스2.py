def charge(M, cnt, remain):
    global res
    if remain < 0:
        return
    if cnt < res:
        if M[0] == -1:
            res = cnt
        else:
            charge(M[1:], cnt, remain - 1)
            charge(M[1:], cnt + 1, M[0] - 1)


T = int(input())
for tc in range(1, T + 1):
    M = list(map(int, input().split()))
    M.append(-1)
    res = M[0] - 1
    charge(M[2:], 0, M[1] - 1)
    print("#{} {}".format(tc, res))
