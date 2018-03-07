def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def selection_sort(arr):
    for i in range(len(arr)):
        m = arr[i]
        idx = i
        for j in range(i, len(arr)):
            if m > arr[j]:
                m = arr[j]
                idx = j
        swap(arr, idx, i)


elements = [3, 23, 45, 2, 21, 102, 1]
selection_sort(elements)
print(elements)
