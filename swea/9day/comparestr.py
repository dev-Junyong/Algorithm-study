T = int(input())

for tc in range(1, T + 1):
    str1, str2 = input(), input()

    len_str1 = len(str1)
    len_str2 = len(str2)

    check_num = 0
    for i in range(len_str2 - len_str1 + 1):
        if str2[i:i + len_str1] == str1:
            check_num = 1

    print("#{} {}".format(tc, check_num))
