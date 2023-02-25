def bubble_sort(arr):
    swap_happened = True # Flag that checks whether a swap happened
    while swap_happened:
        print('Bubble sort status: ' + str(arr))
        swap_happened = False
        # the loop should go to the lastElement - 1 because after the lastElement there is nothing to compare with
        for num in range(len(arr) - 1):
            if arr[num] > arr[num + 1]:
                swap_happened = True
                arr[num], arr[num + 1] = arr[num + 1], arr[num] # Dynamic swapping

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubble_sort(l)
