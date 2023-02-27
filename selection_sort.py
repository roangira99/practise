def selection_sort(arr):
    spot_marker = 0 # Creating the spot marker index and pointing it to the 1st element in the list
    while spot_marker < len(arr): # Outer loop
        for num in range(spot_marker, len(arr)): # Iterating through each number in the array using this inner for loop. 'spot marker' moves the iterator along with it every time it increases by 1
            if arr[num] < arr[spot_marker]: # Performing comparison with the value at the spot marker
                arr[spot_marker], arr[num] = arr[num], arr[spot_marker] # dynamic swapping
        spot_marker += 1
        print(arr)

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
selection_sort(l)



