l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
my_dict = {'py': 'python', 'rb': 'ruby', 'js': 'javascript'}

# # sum of all ints
# sum = 0

# for num in l: # for every value(integer) in the list l
#    sum += num

# print(f"Sum using list: {sum}")

# for num in range(7):
#     # print(num)
#     # print("Heaven")
#     print(l[num])

# # Using range to find the sum of elements in a list
# sum = 0

# for num in range(len(l)):
#    sum += l[num]

# print(f"Sum using range generator: {sum}")

# run_times = int(input("How many times do you want to run? "))
# for num in range(run_times):
#     print(f"Run: {num+1}") # 1 is added to include the last number

# # providing a start and stop value using the range function
# print(list(range(40,70,2)))

# # Iterating through a dictionary
# for item in my_dict.items():
#     print(item)

# # Unpacking the tuples generated after iterating
# for key, value in my_dict.items():
#     print(f"key is {key}, value is {value}")

from random import randint, choice
from string import ascii_lowercase
# Generate random integers between 1 and 100

# l1 = []

# for num in range(100):
#     l1.append(randint(1,100))

# print(l1)

# List comprehension is used in a scenario where you have numbers being 
# generated in a list an orderly way like the previous example above
# List comprehension is a quick way to generate lists
# l1 = [randint(1, 100) for num in range(100)]

# print(l1)

# l2 = [num for num in range(100)]

# print(l2)
 

# l3 = [num**2 for num in range(100)]

# print(l3)

# l4 = [choice(ascii_lowercase) for num in range(100)]

# print(l4)

l5 = list(set([randint(1,1000) for num in range(100)]))
print(l5)
