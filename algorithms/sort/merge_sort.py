def merge_sort(arr):
    if len(arr) > 1 :
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]
        merge_sort(l)
        merge_sort(r)

        i = 0
        j = 0
        k = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[k] = l[i]
                i += 1
                k += 1
            else :
                arr[k] = r[j]
                j += 1
                k += 1

        while i < len(l):
            arr[k] = l[i]
            k += 1
            i += 1

        while j < len(r):
            arr[k] = r[j]
            k += 1
            j += 1


elements = [1, 4, 2, 7, 44, 223, 3, 5, 1020, 512, 765, 304, 6, 8]
merge_sort(elements)
print(elements)