#Frames

# # Frame demo for an immutable data type (int)
# def func_0(start_num):
#     start_num += 1
#     return func_1(start_num)
#
# def func_1(start_num):
#     start_num += 1
#     return start_num
#
# start_num = 1
# print(f"start_num\t-> {start_num}")
# finish_num = func_0(start_num)
# print(f"calc'd_num\t-> {finish_num}")
# print(f"start_num\t-> {start_num}")

# # Frame demo for an immutable data type (int)
# def func_0(other_num):
#     other_num[0] += 1  # having the value at index 0 increment by 1
#     return func_1(other_num)
#
# def func_1(another_num):
#     another_num[0] += 1
#     return another_num
#
# start_num = [1]
# print(f"start_num\t-> {start_num}")
# finish_num = func_0(start_num)
# print(f"calc'd_num\t-> {finish_num}")
# print(f"start_num\t-> {start_num}")
# print(finish_num == start_num)

# If you wanted the function calls to have their own copy of the list, you 
# can use the copy method. This will not reference the original list itself
def func_0(other_num):
    other_num[0] += 1
    return func_1(other_num)

def func_1(another_num):
    another_num[0] += 1
    return another_num

start_num = [1]
print(f"start_num\t-> {start_num}")
finish_num = func_0(start_num.copy()) # method call
print(f"calc'd_num\t-> {finish_num}")
print(f"start_num\t-> {start_num}")
print(finish_num == start_num)

# # You can also pass in a slice of start_num with the whole list
# # using slice notation 
def func_0(other_num):
    other_num[0] += 1
    return func_1(other_num)

def func_1(another_num):
    another_num[0] += 1
    return another_num

start_num = [1]
print(f"start_num\t-> {start_num}")
finish_num = func_0(start_num[:]) # slice notation
print(f"calc'd_num\t-> {finish_num}")
print(f"start_num\t-> {start_num}")
print(finish_num == start_num)