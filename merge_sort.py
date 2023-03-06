def merge_sorted(arr1, arr2):
    sorted_arr = []  
    i, j = 0, 0 # used to iterate through both lists (i for the 1st list and j for the 2nd list)
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1 # After appending the value move the marker
        else:
            sorted_arr.append(arr2[j])
            j += 1
        # print(sorted_arr)
    # Copying to the end of our list for items in the both lists
    while i < len(arr1):
        sorted_arr.append(arr1[i]) # copy the remaining items to the end
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j]) # copy the remaining items to the end
        j += 1
    return sorted_arr

def divide_arr(arr):
    if len(arr) < 2: # base case
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = divide_arr(arr[:middle]) # recursion: calling a function within the same function 
        l2= divide_arr(arr[middle:]) # i.e. divide_arr funtion is called within its code block
        return merge_sorted(l1, l2)


# xxxxxxxxxxxx Program Execution xxxxxxxxxxxx
# l = [8, 6, 2, 5]

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
print(divide_arr(l))
# xxxxxxxxxxxx End Program  xxxxxxxxxxxx

# l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]