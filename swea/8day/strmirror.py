T = int(input())
for tc in range(T):
    str_word = input()
    ans = ''
    for i in range(len(str_word)-1, -1, -1):
        if str_word[i] == 'b':
            ans += 'd'
        elif str_word[i] == 'd':
            ans += 'b'
        elif str_word[i] == 'p':
            ans += 'q'
        else:
            ans += 'p'

    print("#{} {}".format(tc+1, ans))
