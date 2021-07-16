arr = [21, 6, 9, 44, 3, 5, 99, 2, 4]


def selectionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        v = i-1
        for j in range(n):
            if v >= 0 and key < arr[v]:
                arr[v+1] = arr[v]
                arr[v] = key
                v -= 1
            else:
                arr[v+1] = key
    return arr


print(selectionSort(arr))
