def calculator(chk):
    stack_list = []
    i = 0
    while chk[i] != '.':
        if chk[i].isdigit():
            stack_list.append(chk[i])
        elif chk[i] == '+' or chk[i] == '-' or chk[i] == '*' or chk[i] == '/' and len(stack_list) >= 2:
            if chk[i] == '/':
                chk[i] = '//'
            a = stack_list.pop()
            b = stack_list.pop()
            if chk[i] == '+':
                stack_list.append(b + a)
            elif chk[i] == '-':
                stack_list.append(b - a)
            elif chk[i] == '*':
                stack_list.append(b * a)
            elif chk[i] == '//':
                stack_list.append(b // a)
        else:
            return 'error'
        i += 1

    if len(stack_list) == 1:
        return stack_list[0]
    else:
        return 'error'


T = int(input())

for tc in range(1, T + 1):
    str_lst = list(input().split())
    result = calculator(str_lst)
    print("#{} {}".format(tc, result))
