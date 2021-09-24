def game(first, last):
    if first == last:
        return first

    first_stu = game(first, (first+last)//2)
    last_stu = game((first+last)//2+1, last)

    if card_list[last_stu] == 1 and card_list[first_stu] == 3:
        return last_stu
    if card_list[last_stu] == 2 and card_list[first_stu] == 1:
        return last_stu
    if card_list[last_stu] == 3 and card_list[first_stu] == 2:
        return last_stu
    else:
        return first_stu


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card_list = list(map(int, input().split()))
    card_list.insert(0, 0)

    result = game(1, N)
    print("#{} {}".format(tc, result))
