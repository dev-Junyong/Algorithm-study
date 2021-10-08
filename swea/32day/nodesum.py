def dfs(now):
    if now > n + 1:
        return 0
    if tree[now]:
        return tree[now]
    left = now * 2
    right = left + 1
    tree[now] = dfs(left) + dfs(right)
    return tree[now]


T = int(input())
for tc in range(1, T + 1):
    n, m, l = map(int, input().split())
    tree = [0 for _ in range(n + 1)]
    for i in range(m):
        node, val = map(int, input().split())
        tree[node] = val

    if n % 2 == 0:
        tree.append(0)

    ans = dfs(l)
    print("#{} {}".format(tc, ans))
