def inorder(k):
    if k > n:
        return
    if k*2 <= n:
        inorder(k*2)
    ans.append(node[k])
    if k*2+1 <= n:
        inorder(k*2+1)


for tc in range(1, 10+1):
    n = int(input())
    node = [0 for _ in range(n+1)]
    for i in range(n):
        lst = list(input().split())
        node[i+1] = lst[1]
    ans = []
    inorder(1)
    result = ''.join(ans)
    print("#{} {}".format(tc, result))
