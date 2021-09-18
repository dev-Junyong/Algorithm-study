lst = [3, 5, 7, 9, 10, 6]
#  3 5 7 9 10 6 10 9 7 5 3

st = []


def st1(a):
    while st:
        ret = st.pop()

        print(ret, end=' ')


for i in range(len(lst)):
    print(lst[i], end=' ')
    st.append(lst[i])

a = st[::-1]

print(st1(a), end=' ')
