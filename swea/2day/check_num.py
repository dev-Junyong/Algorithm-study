
lst = [3, 2, 7, 5, 9, 11]

flag = 0  # 7을 발견하면 1을 저장하기

for i in range(6):
    if lst[i] == 7:
        flag = 1
        break  # 가장 가까운 loop 를 탈출

if flag == 1:
    print("존재")
else:
    print("안존재")

