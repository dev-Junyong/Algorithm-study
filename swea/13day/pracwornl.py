
# 재귀 연습
def func(level):
    global a
    if level == 3:
        print(a, end='')
        a += 1
        return
    # print("#", end='')
    func(level + 1)
    func(level + 1)
    # print("@", end='')
    return


a = 1
func(0)
print(a)
