def check(a, b):
    lst = {'+': 1, '*': 2, '(': 0}
    if lst[a] <= lst[b]:
        return True
    else:
        return False


T = 10

for tc in range(1, T + 1):
    N = int(input())
    s = input().rstrip()
    i = 0
    n = len(s)
    stack = []
    res = ''
    while i < n:
        if s[i].isdigit():
            res += s[i]
        elif s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            while stack[-1] != '(':
                res += stack.pop()
            stack.pop()
        else:
            while stack and check(s[i], stack[-1]):
                res += stack.pop()
            stack.append(s[i])

        i += 1

    while stack:
        res += stack.pop()

    i = 0
    while i < len(res):
        if res[i].isdigit():
            stack.append(int(res[i]))
        elif res[i] == '+':
            result = stack.pop()+stack.pop()
            stack.append(result)
        elif res[i] == '*':
            result = stack.pop()*stack.pop()
            stack.append(result)
        i += 1

    print("#{} {}".format(tc, *stack))
