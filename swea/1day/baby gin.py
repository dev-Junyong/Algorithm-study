def babygin1(numbers):
    count = [0] * 10
    is_babygin = 0
    for number in numbers:
        count[number] += 1
    idx = 0
    while idx < len(count):
        if count[idx] >= 3:
            count[idx] -= 3
            is_babygin += 1
            continue
        if idx < 8:
            if count[idx] and count[idx + 1] and count[idx + 2]:
                count[idx] -= 1
                count[idx + 1] -= 1
                count[idx + 2] -= 1
                is_babygin += 1
                continue
        if is_babygin == 2:
            return "Baby Gin"
        idx += 1
    if is_babygin != 2:
        return "Lose"


num1 = int(input())
for tc in range(1, num1 + 1):
    lst = list(map(int, input().strip()))
    result = babygin1(lst)
    print(f"#{tc} {result}")
