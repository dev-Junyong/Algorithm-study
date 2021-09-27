
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = [input() for _ in range(N)]
    ans = 'NO'
    for i in range(N):
        for j in range(N):
            if A[i][j] == 'o':  # 오른쪽, 오른쪽 아래 대각선, 아래, 왼쪽 아래 대각선 4개의 돌이 더 있는지 탐색
                for di, dj in [[0,1], [1,1], [1,0], [1,-1]]:
                    cnt = 0
                    for k in range(1,5):
                        ni, nj = i+di*k, j+dj*k
                        if 0 <= ni < N and 0 <= nj < N and A[ni][nj] == 'o':
                           cnt += 1
                        else:  # 4개를 채우기전에 빈칸이 나오면
                            break
                    if cnt == 4:
                        ans = 'YES'
                        break
                if ans == 'YES':
                    break
            if ans == 'YES':
                break

    print("#{} {}".format(tc, ans))

