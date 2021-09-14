
T = int(input())

for tc in range(1, T+1):
    beam_list = list(input())
    total = 0
    steel = 0
    a = 0

    while a < len(beam_list):
        if beam_list[a] == '(' and beam_list[a+1] == ')':
            total += steel
            a += 2
        elif beam_list[a] == '(':
            steel += 1
            a += 1
        else:
            total += 1
            steel -= 1
            a += 1

    print("#{} {}".format(tc, total))
