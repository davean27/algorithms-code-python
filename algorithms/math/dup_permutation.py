def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def dup_perm(arr, result, q=0):
    if q == len(result):
        print(result)
        return

    for i in range(len(arr)):
        swap(arr, i, 0)
        result[q] = arr[0]
        dup_perm(arr, result, q + 1)
        swap(arr, i, 0)

arr = [1, 2, 3]
result = [0] * 2
dup_perm(arr, result)