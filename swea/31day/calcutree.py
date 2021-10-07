def calcu(a, b, oper):
    if oper == '+':
        return int(a) + int(b)
    elif oper == '-':
        return int(a) - int(b)
    elif oper == '*':
        return int(a) * int(b)
    elif oper == '/':
        return int(a) // int(b)


for tc in range(1, 10+1):
    N = int(input())
    tree = [list(input().split()) for _ in range(N)]
    idx = len(tree) - 1
    while idx > -1:
        if len(tree[idx]) != 2:
            a = tree[int(tree[idx][2]) - 1][1]
            b = tree[int(tree[idx][3]) - 1][1]
            oper = tree[idx][1]
            tree[idx][1] = calcu(a, b, oper)
        idx -= 1

    print('#{} {}'.format(tc, int(tree[0][1])))
