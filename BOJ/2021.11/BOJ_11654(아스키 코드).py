
dia_lst = [
    'ABC',
    'DEF',
    'GHI',
    'JKL',
    'MNO',
    'PQRS',
    'TUV',
    'WXYZ'
]

word = input()
res = 0
for i in range(len(word)):
    for j in dia_lst:
        if word[i] in j:
            res += dia_lst.index(j) + 3
print(res)

