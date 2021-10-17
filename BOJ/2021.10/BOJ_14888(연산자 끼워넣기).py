import sys

input = sys.stdin.readline
n = int(input())
num_lst = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_num = -100000000
min_num = 1000000000


def dfs(i, res, add, sub, mul, div):
    global max_num, min_num
    if i == n:
        if res > max_num:
            max_num = res
        if res < min_num:
            min_num = res
        return

    else:
        if add:
            dfs(i + 1, res + num_lst[i], add - 1, sub, mul, div)
        if sub:
            dfs(i + 1, res - num_lst[i], add, sub - 1, mul, div)
        if mul:
            dfs(i + 1, res * num_lst[i], add, sub, mul - 1, div)
        if div:
            dfs(i + 1, int(res / num_lst[i]), add, sub, mul, div - 1)


dfs(1, num_lst[0], add, sub, mul, div)
print(max_num, min_num, sep='\n')
