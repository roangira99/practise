def divide_arr(arr):
    if len(arr) < 2: # base case
        print(f"Base condition reached with {arr[:]}")
        return arr[:]
    else:
        middle = len(arr)//2
        print("Current list to work with:", arr)
        print("Left split:", arr[:middle])
        print("Right split:", arr[middle:])
        l1 = divide_arr(arr[:middle]) # recursion: calling a function within the same function 
        l2= divide_arr(arr[middle:]) # i.e. divide_arr funtion is called within its code block
        # implied return none

# l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]


l = [8, 6, 2, 5]
divide_arr(l)