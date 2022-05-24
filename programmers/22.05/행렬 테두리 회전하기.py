def solution(rows, columns, queries):
    global answer
    answer = []
    arr = [[0] * columns for _ in range(rows)]
    input_num = 1
    for r in range(rows):
        for c in range(columns):
            arr[r][c] = input_num
            input_num += 1
    for query in queries:
        temp_lst = []
        x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        
        for i in arr[x1:x2+1]:
            temp_lst.append(i[y1:y2+1])
        temp_len = len(temp_lst)
        tempf_len = len(temp_lst[0])
        new_arr = rotate(temp_lst, tempf_len, temp_len)
        
        for i in range(temp_len):
            for j in range(tempf_len):
                arr[i + x1][j + y1] = new_arr[i][j]
        
    return answer

def rotate(arr, tempf_len, temp_len):
    new_arr = [[0] * tempf_len for _ in range(temp_len)]
    min_num = 21e8
    
    for i in range(temp_len):
        for j in range(tempf_len):
            chk = arr[i][j]
            if i == 0 and j < tempf_len-1:
                new_arr[i][j+1] = chk
            elif i > 0  and j == 0:
                new_arr[i-1][j] = chk
            elif i == temp_len-1 and j > 0:
                new_arr[i][j-1] = chk
            elif i < temp_len-1 and j == tempf_len-1:
                new_arr[i+1][j] = chk
            else:
                new_arr[i][j] = chk
                continue
            min_num = min(min_num, chk)
    answer.append(min_num)
    return new_arr