def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

# Example usage:
arr = [5, 2, 8, 3, 1, 6, 4]
sorted_arr = quick_sort(arr)
print(sorted_arr)  # [1, 2, 3, 4, 5, 6, 8]
