
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    result = [sum(num_list[i:i+M]) for i in range(N-M+1)]
    ans_result = max(result) - min(result)

    print("#{} {}".format(tc, ans_result))

