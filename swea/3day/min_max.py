
T = int(input())

for t in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    max_num = num_list[0]
    min_num = num_list[0]

    for num in num_list:
        if max_num < num:
            max_num = num
        if num < min_num:
            min_num = num

    result = max_num - min_num
    print(f"#{t} {result}")

