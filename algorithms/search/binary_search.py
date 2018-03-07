def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return -1


elements = [1, 2, 4, 5, 7, 8, 10]
print(binary_search(elements, 2))
print(binary_search(elements, 3))
