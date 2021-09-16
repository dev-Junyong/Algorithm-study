
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    st = []
    print("#{}".format(tc))
    for i in range(n):
        result = input().split()
        if result[0] == 'i':
            st.append(result[1])
        elif result[0] == 'o':
            if st:
                st_pop = st.pop()
                print(st_pop)
            else:
                print('empty')
        elif result[0] == 'c':
            print(len(st))
