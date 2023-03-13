# Iterative version of the bisection search algorithm
def bisection_iter(n, arr): # n is the object and arr is a list in which it will search for n
    start = 0 
    stop = len(arr)-1 # getting the last index
    while start <= stop:
        mid = (start + stop) // 2 # performing integer division to get to the middle of the list
        if n == arr[mid]: # if n is equal to the value in the middle of the list
            return f"{n} found at index {mid}"
        elif n > arr[mid]:
            start = mid + 1 # check list to the right of mid
        else:
            stop = mid - 1 # check list to the left of mid

    return f"{n} not found in list"

# function for creating a list
def create_list(max_val):
    arr = []
    for num in range(1, max_val+1):
        arr.append(num)
    return arr

l = create_list(30) # Create a list with 30 values
for num in range(50): # search for the first 50 values in the list
    print(bisection_iter(num, l))