for tc in range(1, 11):
    dump_num = int(input())
    box_list = list(map(int, input().split()))
    result = 0

    for i in range(dump_num):
        max_loc = box_list.index(max(box_list))
        min_loc = box_list.index(min(box_list))
        box_list[max_loc] -= 1
        box_list[min_loc] += 1
    result = max(box_list) - min(box_list)

    print("#{} {}".format(tc, result))


