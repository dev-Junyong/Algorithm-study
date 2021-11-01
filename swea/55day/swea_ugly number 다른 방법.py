def uglynum(input_num):
    check = [0] * input_num
    check[0] = 1
    i2 = i3 = i5 = 0
    nums2 = 2
    nums3 = 3
    nums5 = 5
    for j in range(1, input_num):
        check[j] = min(nums2, nums3, nums5)
        if check[j] == nums2:
            i2 += 1
            nums2 = check[i2] * 2
        if check[j] == nums3:
            i3 += 1
            nums3 = check[i3] * 3
        if check[j] == nums5:
            i5 += 1
            nums5 = check[i5] * 5
    return check[-1]


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    res = []
    for i in lst:
        num = uglynum(i)
        res.append(str(num))

    print("#{} ".format(tc), end='')
    print(" ".join(res))
