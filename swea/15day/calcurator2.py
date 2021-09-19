
for tc in range(1, 10+1):
    n = int(input())
    str_list = list(map(str, input()))
    num_list = []
    stack = []
    result = 0
    tmp = 1

    for i in str_list:
        if i == '+' or i == '*':
            stack.append(i)
        else:
            num_list.append(int(i))

    for j in range(int(n/2)):
        if j != int(n/2)-1:
            if stack[j] == '+':
                if tmp != 1:
                    tmp *= num_list[j]
                    result += tmp
                    tmp = 1
                else:
                    result += num_list[j]
            else:
                tmp *= num_list[j]
        else:
            if stack[j] == '+':
                if tmp != 1:
                    tmp *= num_list[j]
                    result += tmp
                else:
                    result += num_list[j]
                result += num_list[j+1]
            else:
                tmp *= num_list[j]*num_list[j+1]
                result += tmp
    print("#{} {}".format(tc, result))
