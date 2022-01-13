
N = int(input())

cnt = 0
num_six = 666
while True:
    if '666' in str(num_six):
        cnt += 1
    if cnt == N:
        print(num_six)
        break
    num_six += 1
