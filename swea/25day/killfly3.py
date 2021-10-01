
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = int(-21e8)  

    dy = [-1, 1, 0, 0] 
    dx = [0, 0, -1, 1]


    dr = [-1, 1, 1, -1]  
    dc = [1, 1, -1, -1]
    for i in range(N-M+1):  
        for j in range(N-M+1):
            tmp_sum1 = 0  
            tmp_sum2 = 0  
            tmp_total = 0
            for a in range(M): 
                for b in range(M):
                    tmp_sum1 += arr[i+a][j+(M//2)+1]

            tmp_total += arr[i][j]

            if max_sum < tmp_total:
                max_sum = tmp_total

    print("#{} {}".format(tc, max_sum))
