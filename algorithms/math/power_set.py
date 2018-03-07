def power_set(arr, result, idx=0):
    if idx == len(arr):
        print(result)
        return

    result.append(arr[idx])
    power_set(arr, result, idx+1)
    result.pop()
    power_set(arr, result, idx+1)


elements = [1, 2, 3]
r = list()
power_set(elements, r)
