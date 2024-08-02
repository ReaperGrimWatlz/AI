def bubble_sort(arr):

    """

    Sorts an array in ascending order using the Bubble Sort algorithm.


    Args:

        arr (list): The input array to be sorted.


    Returns:

        list: The sorted array.

    """

    n = len(arr)


    for i in range(n-1):

        # Create a flag that will allow the function to terminate early if there's nothing left to sort

        swapped = False


        # Start looking at each item of the list one by one, comparing it with its adjacent value

        for j in range(n-i-1):

            # If we find an element that is greater than its adjacent element, then swap them

            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]

                swapped = True


        # If no two elements were swapped in the inner loop, the list is sorted and we can terminate

        if not swapped:

            break


    return arr


# Example usage:

arr = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", arr)

print("Sorted array:", bubble_sort(arr))
