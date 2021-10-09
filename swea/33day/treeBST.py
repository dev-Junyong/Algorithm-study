def chktree(now):
    global cnt
    if now <= n:
        chktree(now * 2)
        tree[now] = cnt
        cnt += 1
        chktree(now * 2 + 1)
        return cnt
    else:
        return cnt


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    tree = [0 for _ in range(n + 1)]
    cnt = 1
    chktree(1)
    print("#{} {} {}".format(tc, tree[1], tree[n // 2]))
