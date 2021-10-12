# import sys
#
# sys.stdin = open("input.txt", "r")

chk_code = {211: 0, 221: 1,
            122: 2, 411: 3,
            132: 4, 231: 5,
            114: 6, 312: 7,
            213: 8, 112: 9
            }

code = {'0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
        }


def cal(idx):
    global res
    while idx > 56:
        if arr[r][idx] == '1' and arr[r - 1][idx] == '0':
            lst = [0] * 8
            for k in range(7, -1, -1):
                num1 = num2 = num3 = 0
                while arr[r][idx] == '1':
                    num3 += 1
                    idx -= 1
                while arr[r][idx] == '0':
                    num2 += 1
                    idx -= 1
                while arr[r][idx] == '1':
                    num1 += 1
                    idx -= 1
                while arr[r][idx] == '0':
                    idx -= 1
                min_num = min(num1, num2, num3)
                lst[k] = chk_code[(num1 // min_num) * 100 + (num2 // min_num) * 10 + num3 // min_num]
            chk_num = (lst[0] + lst[2] + lst[4] + lst[6]) * 3 + (lst[1] + lst[3] + lst[5] + lst[7])
            if chk_num % 10 == 0:
                res += sum(lst)
            idx += 1
        idx -= 1
    return res


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    MAP = [input() for _ in range(N)]
    arr = [''] * N

    for i in range(N):
        for j in range(M):
            arr[i] += code[MAP[i][j]]
    de = -1
    res = 0
    for r in range(len(arr)):
        idx = M * 4 - 1
        cal(idx)

    print('#{} {}'.format(tc, res))
