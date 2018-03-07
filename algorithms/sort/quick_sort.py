def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, l, r):
    pivot = arr[l]
    idx = l
    while l <= r:
        while l <= r and arr[l] <= pivot:
            l += 1
        while l <= r and arr[r] >= pivot:
            r -= 1

        if l <= r:
            swap(arr, l, r)
            l += 1
            r -= 1

    swap(arr, idx, r)
    return r


def quick_sort_internal(arr, l, r):
    if l < r:
        sp = partition(arr, l, r)
        quick_sort_internal(arr, l, sp - 1)
        quick_sort_internal(arr, sp + 1, r)


def quick_sort(arr):
    quick_sort_internal(arr, 0, len(arr) - 1)


elements = [1, 4, 2, 7, 44, 223, 3, 5, 1020, 512, 765, 304, 6, 8]
quick_sort(elements)
print(elements)
