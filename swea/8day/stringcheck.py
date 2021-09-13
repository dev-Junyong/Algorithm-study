
for tc in range(1, 10+1):
    TC = int(input())
    find_str = input()
    sen_str = input()
    cnt = sen_str.count(find_str)

    print("#{} {}".format(TC, cnt))

"""
for t in range(1,11):
    N = int(input())
    word =input()
    sentence = input()
    cnt = 0
    for i in range(len(sentence)-len(word)+1):
        for j in range(i+len(word)+1):
            if sentence[i:j] == word:
                cnt +=1
    print(f'#{N} {cnt}')
"""