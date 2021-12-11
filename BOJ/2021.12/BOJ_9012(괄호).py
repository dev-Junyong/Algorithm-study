T = int(input())

for _ in range(T):
    stack = []
    res = True

    for i in input():
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                res = False
                break
    if stack:
        res = False

    if res:
        print('YES')
    else:
        print('NO')
