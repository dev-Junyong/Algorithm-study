T = int(input())

for tc in range(1, T + 1):
    num_str = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    n, length = input().split()
    str_list = list(input().split())

    check_chk = []
    num_len = int(length)

    for i in range(num_len):
        check_chk.append(num_str.index(str_list[i]))

    check_chk.sort()

    for j in range(num_len):
        check_chk[j] = num_str[check_chk[j]]

    print("{}".format(n))
    print(*check_chk)

