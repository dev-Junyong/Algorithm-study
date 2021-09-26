
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    quene = lst + [0]*2000
    front = 0
    rear = N

    for j in range(M):
        quene[rear] = quene[front]
        front += 1
        rear += 1

    print("#{} {}".format(tc, quene[front]))
