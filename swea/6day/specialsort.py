T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    for i in range(10):
        if not i & 1:
            max_id = i
            for j in range(i + 1, N):
                if num_list[j] > num_list[max_id]:
                    max_id = j
            num_list[i], num_list[max_id] = num_list[max_id], num_list[i]

        else:
            min_id = i
            for k in range(i + 1, N):
                if num_list[k] < num_list[min_id]:
                    min_id = k
            num_list[i], num_list[min_id] = num_list[min_id], num_list[i]
    result = num_list[:10]

    print("#{}".format(tc), *result)

