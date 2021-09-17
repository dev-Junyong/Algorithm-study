
def dfs(result):
    global cnt
    if result == 99:
        cnt = 1
        return

    for i in range(len(cha_map)):
        if cha_map[i][0] == result and not num_list[cha_map[i][0]]:
            num_list[cha_map[i][0]] = 1
            dfs(cha_map[i][1])
            num_list[cha_map[i][0]] = 0


for tc in range(10):
    T, N = map(int, input().split())

    map_list = list(map(int, input().split()))
    cha_map = list(zip(map_list[::2], map_list[1::2]))
    cnt = 0
    num_list = [0]*100
    dfs(0)

    print("#{} {}".format(T, cnt))
