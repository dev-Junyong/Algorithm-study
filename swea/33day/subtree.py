def inorder(node):
    global cnt
    if node == 0: return

    cnt += 1
    inorder(tree[0][node])
    inorder(tree[1][node])


T = int(input())
for tc in range(1, T+1):
    e, n = map(int, input().split())
    tmp_lst = list(map(int, input().split()))
    tree = [[0 for _ in range(e+2)] for _ in range(2)]

    for i in range(e):
        num1, num2 = tmp_lst[i*2], tmp_lst[i*2+1]
        if tree[0][num1] == 0:
            tree[0][num1] = num2
        else:
            tree[1][num1] = num2

    cnt = 0
    inorder(n)
    print("#{} {}".format(tc, cnt))



