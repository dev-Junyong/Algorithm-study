def is_valid(s1, s2):
    eval = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    if eval[s1] > eval[s2]:
        return True
    else:
        return False


T = int(input())
for tc in range(1, T + 1):
    s = input().rstrip()
    stack = []
    n = len(s)
    i = 0
    print("#{} ".format(tc), end='')
    while i < n:
        if ord('0') <= ord(s[i]) <= ord('9'):
            print(s[i], end='')
        elif s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            while stack[-1] != '(':
                print(stack.pop(), end='')
            stack.pop()
        else:
            while stack and not is_valid(s[i], stack[-1]):
                print(stack.pop(), end='')
            stack.append(s[i])
        i += 1

    while stack:
        print(stack.pop(), end='')
    print()
