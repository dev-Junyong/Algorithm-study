import sys


def dfs(tmp, depth):
    global res
    if depth >= n:
        return

    if tmp + arr[depth] == s:
        res += 1
    dfs(tmp, depth+1)
    dfs(tmp+arr[depth], depth + 1)


n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
res = 0
dfs(0, 0)
print(res)

