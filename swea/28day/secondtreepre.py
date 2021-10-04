def preorder(root):
    if root == 0 or root > V:
        return
    if root:
        print(root, end=' ')
    preorder(left[root])
    preorder(right[root])


T = int(input())
for tc in range(1, T+1):
    V = int(input())
    left = [0 for _ in range(V+1)]
    right = [0 for _ in range(V+1)]
    root = 1
    result = []
    for i in range(V-1):
        p, s = map(int, input().split())
        if left[p] == 0:
            left[p] = s
        else:
            right[p] = s

    print('#{}'.format(tc), end=' ')
    preorder(root)
    print()
