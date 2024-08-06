def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        swapped = False
        
        # Start looking at each item of the list one by one, comparing it with its adjacent value
        for j in range(0, n-i-1):
            # If we find an element that is greater than its adjacent element, then swap them
            if arr[j] > arr[j+1]:
                # Swap values
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Set the flag to True so we'll loop again
                swapped = True
        
        # If no two elements were swapped in inner loop, the list is sorted
        if not swapped:
            break
    
    return arr

# Example usage
arr = [8,6,5,9,0,8,1,7,3,2,1]
print("Original array:", arr)
print("Sorted array:", bubble_sort(arr))