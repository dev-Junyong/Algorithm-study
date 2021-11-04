from collections import deque

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    res = 0
    visited = [0] * 1000001
    queue = deque()
    queue.append((n, 0))
    while queue:
        flag, idx = queue.popleft()
        if flag == m:
            res = idx
            break
        for i in range(4):
            if i == 0:
                if 1 <= flag + 1 <= 1000000 and visited[flag + 1] == 0:
                    queue.append((flag + 1, idx + 1))
                    visited[flag + 1] = 1
            elif i == 1:
                if 1 <= flag - 1 <= 1000000 and visited[flag - 1] == 0:
                    queue.append((flag - 1, idx + 1))
                    visited[flag - 1] = 1
            elif i == 2:
                if 1 <= flag * 2 <= 1000000 and visited[flag * 2] == 0:
                    queue.append((flag * 2, idx + 1))
                    visited[flag * 2] = 1
            elif i == 3:
                if 1 <= flag - 10 <= 1000000 and visited[flag - 10] == 0:
                    queue.append((flag - 10, idx + 1))
                    visited[flag - 10] = 1
    print("#{} {}".format(tc, res))
