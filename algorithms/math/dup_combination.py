def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def dup_comb(arr, r, q=0, idx=0):
    if len(r) == q:
        print(r)
        return

    if idx >= len(arr):
        return

    r[q] = arr[idx]
    dup_comb(arr, r, q+1, idx)
    r[q] = arr[idx]
    dup_comb(arr, r, q, idx+1)


elements = [1, 2, 3]
result = [0] * 2
dup_comb(elements, result)
