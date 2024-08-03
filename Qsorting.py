def quicksort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    sorte=sorted([arr[0], arr[mid], arr[-1]])
    pivot =sorte[1]

    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quicksort(less) + equal + quicksort(greater)