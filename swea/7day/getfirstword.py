
def first_word():
    n = int(input())
    str_list = input().split()
    for i in range(n):
        str_list[i] = str_list[i][0].upper()

    ans = ''.join(str_list)

    return ans


T = int(input())

for tc in range(1, T+1):
    print("#{} {}".format(tc, first_word()))
