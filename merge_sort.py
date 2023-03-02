def merge_sorted(arr1,arr2): # takes in two sorted lists
    print("Merge function called with lists below:")
    print(f"left: {arr1} and right: {arr2}")
    sorted_arr = []
    i, j = 0, 0 # indices i & j used to iterate through the two lists
    while i < len(arr1) and j < len(arr2): # breaks out of program when we get to the end of one of the lists
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1 # move index by 1 if an append occurs
        else:
            sorted_arr.append(arr2[j])
            j += 1
        print(sorted_arr)
    # Grab the value that is less than the length of the array it is working with and paste any elements that are remaining
    while i < len(arr1):
        sorted_arr.append(arr1[i]) # copy the remaining items to the end
        i += 1 

    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    return sorted_arr

# xxxxxxxxxxx Program Execution xxxxxxxxxxx
l1 = [2,4,6,8,11,15,16]
l2 = [1,3,5,7,8,9,10]
print(f"Merged list: {merge_sorted(l1, l2)}")