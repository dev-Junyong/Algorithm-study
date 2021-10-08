
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0]
    lst = list(map(int, input().split()))
    for i in range(N):
        tree.append(lst[i])
        now = len(tree)-1
        while now > 1 and tree[now] < tree[now//2]:
            tree[now], tree[now // 2] = tree[now // 2], tree[now]
            now //= 2

    tmp = N
    res = 0
    while tmp >= 1:
        tmp //= 2
        res += tree[tmp]

    print('#{} {}'.format(tc, res))

