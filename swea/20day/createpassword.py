
for tc in range(1, 10+1):
    T = int(input())
    lst = list(map(int, input().split()))
    quene = lst + [0]*100000
    front = 0
    rear = 7

    while quene[rear]:
        for i in range(1, 6):
            quene[rear+1] = quene[front] - i
            front += 1
            rear += 1
            if quene[rear] <= 0:
                quene[rear] = 0
                break

    print("#{}".format(T), end=' ')
    for j in range(8):
        print(quene[j+front], end=' ')
    print()
