
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card_list = list(map(int, list(input())))
    cnt_list = [0]*10

    for i in card_list:
        cnt_list[i] += 1
    max_num = 0
    max_cnt = 0

    for i in range(9, -1, -1):
        if cnt_list[i] > max_cnt:
            max_cnt = cnt_list[i]
            max_num = i

    print("#{} {} {}".format(tc, max_num, max_cnt))

