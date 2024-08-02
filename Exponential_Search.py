def hash_table_search(arr, target):
    hash_table = {x: i for i, x in enumerate(arr)}
    return hash_table.get(target, -1)  # return -1 if not found
def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2

    return binary_search(arr, target, i // 2, min(i, len(arr)))

def binary_search(arr, target, low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # not found
