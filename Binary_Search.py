def binary_search(arr, target):
    """
    Searches for an element in a sorted array using Binary Search.

    Args:
        arr (list): The sorted array to search in.
        target: The element to search for.

    Returns:
        int: The index of the element if found, -1 otherwise.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # not found

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9
index = binary_search(arr, target)

if index!= -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found in the array")
