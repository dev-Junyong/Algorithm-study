def mergesort(arr):
    global cnt
    if len(arr) == 1:
        return arr
    else:
        m = len(arr) // 2  # 문제 조건
        left = arr[:m]
        right = arr[m:]
        left = mergesort(left)
        right = mergesort(right)
        idx_l = 0
        idx_r = 0
        i = 0  # 병합된 배열 idx
        if left[-1] > right[-1]:
            cnt += 1
        # while idx_l < len(left) or idx_r < len(right):
        while i < len(arr):
            if idx_l < len(left) and idx_r < len(right):
                if left[idx_l] < right[idx_r]:
                    arr[i] = left[idx_l]
                    idx_l += 1
                else:
                    arr[i] = right[idx_r]
                    idx_r += 1
            elif idx_l < len(left):
                arr[i] = left[idx_l]
                idx_l += 1
            else:
                arr[i] = right[idx_r]
                idx_r += 1
            i += 1
        return arr


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = mergesort(arr)
    print("#{} {} {}".format(tc, arr[N//2], cnt))
