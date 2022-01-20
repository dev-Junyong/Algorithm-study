import sys
input = sys.stdin.readline
N = int(input())

stack = []
for i in range(N):
    comm = input().split()

    if comm[0] == 'push':
        stack.append(comm[1])
    if comm[0] == 'pop':
        if len(stack):
            flag = stack.pop()
            print(flag)
        else:
            print(-1)
    if comm[0] == 'size':
        print(len(stack))
    if comm[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    if comm[0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
