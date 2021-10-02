
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    card = list(map(str, input().split()))
    mid = n // 2
    result = []
    idx = 1
    for i in range(n):
        if n % 2 == 0:
            if i < mid:
                result.append(card[i])
            else:
                result.insert(idx, card[i])
                idx += 2
        else:
            if i < mid+1:
                result.append(card[i])
            else:
                result.insert(idx, card[i])
                idx += 2

    print("#{} ".format(tc), end='')
    print(*result)
