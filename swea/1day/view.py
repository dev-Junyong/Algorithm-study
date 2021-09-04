
for n in range(10):
    b_num = int(input())

    b_list = list(map(int, input().split()))
    result = 0

    for i in range(2, len(b_list)-1):
        if b_list[i-1] < b_list[i] and b_list[i+1] < b_list[i]:

            if b_list[i] - b_list[i-1] < b_list[i] - b_list[i+1]:
                keep_result = b_list[i] - b_list[i-1]
            else:
                keep_result = b_list[i] - b_list[i+1]

            if b_list[i-2] < b_list[i] and b_list[i+2] < b_list[i]:
                if b_list[i] - b_list[i-2] < b_list[i] - b_list[i+2]:
                    keep_new = b_list[i] - b_list[i-2]
                else:
                    keep_new = b_list[i] - b_list[i+2]

                if keep_new < keep_result:
                    result += keep_new
                else:
                    result += keep_result
        else:
            continue

    print(f"#{n+1} {result}")
