arr = [5, 3, 2, 7, 9, 8, 6]

for i in range(len(arr) - 1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)
