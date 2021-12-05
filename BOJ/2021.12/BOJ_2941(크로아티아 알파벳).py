lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

tmp = input()
for i in lst:
    tmp = tmp.replace(i, '0')
print(len(tmp))
