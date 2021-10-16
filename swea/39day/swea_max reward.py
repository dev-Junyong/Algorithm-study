
T = int(input())
for tc in range(1, T + 1):
    arr, n = input().split()
    n = int(n)
    arr_len = len(arr)
    res = 0
    num_set = {arr}
    num1_set = set()
    for _ in range(n):
        while num_set:
            st = list(num_set.pop())
            for i in range(arr_len):
                for j in range(i + 1, arr_len):
                    st[i], st[j] = st[j], st[i]
                    num1_set.add(''.join(st))
                    st[i], st[j] = st[j], st[i]
        num_set, num1_set = num1_set, num_set
    res = max(map(int, num_set))
    print('#{} {}'.format(tc, res))


