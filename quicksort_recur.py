def quicksort(arr):
    """
    Input: Unsorted list of integers
    Returns sorted list of integers using Quicksort
    Note: This is not an in-place implementation
    """
    if len(arr) < 2: # base case
        return arr
    else:
        pivot = arr[-1] # in this case the pivot is the last elemet
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num) # append to smaller list
            elif num == pivot:
                equal.append(num) # append to equal list
            else:
                larger.append(num) # append to larger  list
        # recursively run the quicksort function on the smaller and larger lists to get a fully sorted list
        return quicksort(smaller) + equal + quicksort(larger) # concatenating the three objects returns a single list instead of three separate lists in tuple format


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
print(quicksort(l))