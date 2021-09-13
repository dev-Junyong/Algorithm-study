def is_pattern(start_idx, pn):
    if start_idx + pn - 1 >= len(lst): return 0  # 인덱스 초과 방지
    for i in range(pn):
        # lst[start_idx + i] vs pattern[i]
        if lst[start_idx + i] != pattern[i]:
            return 0

    return 1


lst = [7, 1, 2, 5, 3, 2, 7, 9, 1, 2, 5]
pattern = [1, 2, 5]

cnt = 0
for i in range(len(lst)):
    ret = is_pattern(i, 3)
    if ret == 1:
        cnt += 1

print(cnt)
