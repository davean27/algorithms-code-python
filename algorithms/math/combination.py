def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def comb(arr, result, q=0, idx=0):
    if len(result) == q:
        print(result)
        return

    if idx >= len(arr):
        return

    result[q] = arr[idx]
    comb(arr, result, q, idx + 1)
    result[q] = arr[idx]
    comb(arr, result, q + 1, idx + 1)


arr = [1, 2, 3]
result = [0] * 2
comb(arr, result)