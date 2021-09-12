T = int(input())

for tc in range(1, T + 1):
    word = str(input())

    new_word = ''

    for i in word:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
            new_word += i

    print("#{} {}".format(tc, new_word))
