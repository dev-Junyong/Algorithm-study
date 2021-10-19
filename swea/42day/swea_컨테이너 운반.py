T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    box = list(map(int, input().split()))
    car = list(map(int, input().split()))
    res = 0
    for i in range(M):
        tmp = []  # 용량 작을 때, 넣을거야
        for j in range(N):
            if car[i] >= box[j]:
                tmp.append(box[j])
        if len(tmp) > 0:
            res += max(tmp)
            for k in range(N):
                if box[k] == max(tmp):
                    box[k] = 0
                    break

    print("#{} {}".format(tc, res))
