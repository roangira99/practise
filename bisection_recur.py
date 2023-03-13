# recursive implementation of binary search
def bisection_recur(n, arr, start, stop):
    if start > stop:
        return f"{n} not found in list"
    else:
        mid = (start + stop) // 2
        if n == arr[mid]: # if n is equal to the value in the middle of the list
            return f"{n} found at index {mid}"
        elif n > arr[mid]:
            return bisection_recur(n, arr, mid + 1, stop) # recursive call of the function
        else:
            return bisection_recur(n, arr, start, mid -1)

def create_list(max_val):
    arr = []
    for num in range(1, max_val+1):
        arr.append(num)
    return arr

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in range(16):
    print(bisection_recur(num, l, 0, len(l)-1))
           