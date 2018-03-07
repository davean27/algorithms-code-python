def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)


elements = [1, 4, 2, 10, 34, 23, 3, 7, 6]
bubble_sort(elements)
print(elements)
