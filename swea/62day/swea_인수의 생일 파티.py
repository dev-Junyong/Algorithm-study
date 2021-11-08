from collections import deque


def func1(k):
    q = deque()
    q.append(k)
    while q:
        tmp = q.popleft()
        for i in range(m):
            if arr[i][0] == tmp:
                if visited1[arr[i][1]] > visited1[tmp] + arr[i][2]:
                    visited1[arr[i][1]] = visited1[tmp] + arr[i][2]
                    q.append(arr[i][1])


def func2(k):
    q = deque()
    q.append(k)
    while q:
        tmp = q.popleft()
        for i in range(m):
            if arr[i][1] == tmp:
                if visited2[arr[i][0]] > visited2[tmp] + arr[i][2]:
                    visited2[arr[i][0]] = visited2[tmp] + arr[i][2]
                    q.append(arr[i][0])


T = int(input())
for tc in range(1, T + 1):
    n, m, x = map(int, input().split())
    arr = []
    for i in range(m):
        s, e, c = map(int, input().split())
        arr.append((s, e, c))
    arr.sort(key=lambda x: x[0])
    visited1 = [int(21e8)] * (n + 1)
    visited1[x] = 0
    visited2 = [int(21e8)] * (n + 1)
    visited2[x] = 0
    func1(x)
    func2(x)
    res = []
    for i in range(1, n + 1):
        res.append(visited1[i] + visited2[i])

    print('#{} {}'.format(tc, max(res)))
