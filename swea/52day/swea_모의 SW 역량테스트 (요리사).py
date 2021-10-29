def divide(idx, sel):
    if sel == n // 2:
        divided.append(selec[:])
        return
    for i in range(idx, n):
        if not visited[i]:
            selec[sel] = i
            visited[i] = True
            divide(i, sel + 1)
            visited[i] = False


def check_sum(_num_list):
    res = 0
    for i in range(len(_num_list) - 1):
        for j in range(i + 1, len(_num_list)):
            res += arr[_num_list[i]][_num_list[j]]
            res += arr[_num_list[j]][_num_list[i]]
    return res


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    selec = [0] * (n // 2)
    visited = [0] * n
    divided = []
    divide(0, 0)
    min_num = int(21e8)
    for i in range(len(divided)):
        rem_lst = []
        tmp_idx = 0
        for num in range(n):
            if tmp_idx >= n // 2:
                rem_lst.append(num)
            else:
                if divided[i][tmp_idx] == num:
                    tmp_idx += 1
                else:
                    rem_lst.append(num)
        start = check_sum(divided[i])
        flag = check_sum(rem_lst)
        min_num = min(min_num, abs(start - flag))

    print("#{} {}".format(tc, min_num))
