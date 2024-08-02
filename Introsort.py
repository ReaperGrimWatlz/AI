def introsort(arr):
    max_depth = 2 * len(arr).bit_length()
    introsort_helper(arr, 0, len(arr), max_depth)

def introsort_helper(arr, start, end, max_depth):
    if end - start <= 16:
        insertion_sort(arr, start, end)
    elif max_depth == 0:
        heapsort(arr, start, end)
    else:
        p = partition(arr, start, end)
        introsort_helper(arr, start, p, max_depth - 1)
        introsort_helper(arr, p + 1, end, max_depth - 1)

def partition(arr, start, end):
    pivot = arr[start]
    i = start + 1
    j = end - 1

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[start], arr[j] = arr[j], arr[start]
            return j

def insertion_sort(arr, start, end):
    for i in range(start + 1, end):
        key = arr[i]
        j = i - 1
        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def heapsort(arr, start, end):
    build_heap(arr, start, end)
    for i in range(end - 1, start, -1):
        arr[start], arr[i] = arr[i], arr[start]
        heapify(arr, start, i, start)

def build_heap(arr, start, end):
    for i in range((end - start) // 2 - 1, -1, -1):
        heapify(arr, start, end, start + i)

def heapify(arr, start, end, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < end - start and arr[start + left] > arr[start + largest]:
        largest = left
    if right < end - start and arr[start + right] > arr[start + largest]:
        largest = right

    if largest != i:
        arr[start + i], arr[start + largest] = arr[start + largest], arr[start + i]
        heapify(arr, start, end, start + largest)

# Example usage:
arr = [5, 2, 8, 3, 1, 6, 4]
introsort(arr)
print(arr)  # [1, 2, 3, 4, 5, 6, 8]
