
lst = [3, 7, 5, 9, 2, 8]

st = []
for i in range(len(lst)):
    print(lst[i], end=' ')
    st.append(lst[i])

while st:
    ret = st.pop()

    print(ret, end=' ')
