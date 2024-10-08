import numpy as np

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # not found

# Create a sorted NumPy array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Search for a target value
target = 5
index = binary_search(arr, target)

if index != -1:
    print(f"Found {target} at index {index}")
else:
    print(f"{target} not found in the array")
