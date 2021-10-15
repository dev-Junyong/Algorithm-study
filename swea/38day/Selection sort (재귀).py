def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def selectionsort(a):
    for i in range(len(a) - 1):
        min_num = i

        for j in range(i + 1, len(a)):
            if a[j] < a[min_num]:
                min_num = j
        swap(a, min_num, i)


if __name__ == '__main__':
    A = [3, 5, 8, 4, 1, 9, -2]

    selectionsort(A)

    print(A)
