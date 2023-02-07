# Lists

# my_list = [15, 6, 7, 8, 35, 14, 4, 10]
# my_strings_list = ["comp sci", "physics", "elec engr", "philosophy"]
# print(f"Ints: {my_list}")
# print(f"Strings: {my_strings_list}")
# print("Sorting...")
# the sorted function does not sort the list in place and that is why the result 
# has to be printed
# sorted_list = sorted(my_list) 
# print(sorted_list)
# print(f"Sorted Ints: {my_list}")

# Unlike the sorted function, the sort method sorts a list in place
# my_list.sort()
# print(f"Sorted Ints: {my_list}")

# Finding information about the list
# my_list = [15, 6, 7, 8, 35, 12, 14, 4, 7, 7, 10]
# my_strings_list = ["comp sci", "physics", "elec engr", "philosophy"]
# print(f"Ints: {my_list}")
# print(f"Strings: {my_strings_list}")
# print("Finding info...")
# print("philosophy" in my_strings_list)
# print(38 in my_list)

# Finding the location of an object in a list
# print(my_strings_list.index("philosophy"))

# Finding the length of a list
# print(len(my_list))
# print(len(my_strings_list))

# Finding the value of the last element in the list using the len() function
# print(my_list[len(my_list)-1]) # OR
# print(my_list[-1])

# Finding the minimum and maximum value within the list
# print(min(my_list))
# print(max(my_list))

# Seeing the methods available to your object or data type
# print(dir(my_list))

# Counting the number of occurences of a value in a list
# print(my_list.count(7))

# Exercise
# my_list = [15, 6, 7, 8, 35, 12, 4, 10, 15]
# my_new_list = my_list
# my_new_list.sort()
# print(my_list == my_new_list)


# Adding items to and removing items from a list
# append(), insert(), extend()
# my_list = [15, 6, 7, 8, 35, 12, 4, 10, 15]
# my_strings_list = ["comp sci", "physics", "elec engr", "philosophy"]
# my_new_list = ["art", "econ"]
# print(f"Ints: {my_list}")
# print(f"Strings: {my_strings_list}")
# print("Add/remove...")

# # append() method adds a value to the end of the list
# my_list.append(93)
# print(my_list)

# # the insert method puts a value at a specific index in the list
# # you provide the index first, then the object
# my_list.insert(1, 56)
# print(my_list)

# # extend is used to insert a list into an exsisting list
# my_strings_list.extend(my_new_list)
# print(my_strings_list)

# Removing values from an existing list
# pop(), remove()
# my_strings_list.remove("philosophy") # the remove method doesn't return anything
# print(my_strings_list)

# pop() removes the last element in the list
# my_strings_list.pop()
# print(my_strings_list)
# You can also provide the index of the element you want to be removed
# pop() also returns the value it removes
# print(my_strings_list.pop(2))
# print(my_strings_list)

# Working with sublists
my_list = [15, 6, 7, 8, 35, 12, 4, 10, 15]
# indices   0, 1, 2, 3,  4,  5, 6,  7,  8 
my_strings_list = ["comp sci", "physics", "elec engr", "philosophy"]
my_new_list = ["art", "econ"]
print(f"Ints: {my_list}")
print(f"Strings: {my_strings_list}")
print("Sublists...")
# print(my_list[-1])
# my_list[-1] = 544
# print(my_list)

# Slicing
# the stop index will not be included in the slice
# print(my_list[0:4]) # Or
# print(my_list[:4]) 
# print(my_list)

# # printing the full list
# print(my_list[:])

# # providing a step size to the list
# print(my_list[::2])

# # starting from the end of the list and moving backwards
# print(my_list[::-1])
# OR 
# Use the reverse method
# my_list.reverse()
# print(my_list)

# Iteration
# The for loop
for item in my_list:
    print(item)
