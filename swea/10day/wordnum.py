
T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    check_list = []
    for i in str1:
        check_list.append(str2.count(i))

    print("#{} {}".format(tc, max(check_list)))
