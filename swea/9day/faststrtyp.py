def min_type():
    cnt = 0
    check_id = 0
    while check_id < len_a:
        if A[check_id] == B[0]:
            if A[check_id:check_id + len_b] == B:
                cnt += 1
                check_id += len_b
            else:
                cnt += 1
                check_id += 1
        else:
            cnt += 1
            check_id += 1
    return cnt


T = int(input())

for tc in range(1, T + 1):
    A, B = input().split()
    len_a = len(A)
    len_b = len(B)

    result = min_type()

    print("#{} {}".format(tc, result))
