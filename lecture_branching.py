 # Branching and control flow

# boolean operators
# truth_condition = False

# if truth_condition:
#     print("Truth")

# choice = '2'

# if choice == '1':
#     print("You have chosen option 1")
# elif choice == '2':
#     print("You have chosen option 2")
# else:
#     print("You have made an invalid choice")

# choice = '1'
# made_payment = 'False'

# if choice == '1' and made_payment == 'True':
#     print("You have chosen option 1")
# elif choice == '2':
#     print("You have chosen option 2")
# else:
#     print("You have made an invalid choice")

# made_payment = True
# a = "Please pay monthly premium"
# b = "Welcome to your homepage"

# if not made_payment:
#     print(a)
# else:
#     print(b)

# i = 7
# j = 7
# k = 7

# comparison operators 
# if i < j and i < k:
#     print("i is less than j and k")
# elif i == j or i == k:
#     print("i is equal to either j or k")
# elif i == j and i == k:
#     print("i is equal to j and k")
# else:
#     print("Something else")

# expressing an if-else statement using ternary operators
course = 'javascript'
a = 'enrolled in python course'
b = 'enrolled in some other course'

# print(a) if course == 'python' else print(b) # ternary operator use

made_payment = True
a = "Please pay monthly premium"
b = "Welcome to your homepage"
print(a) if not made_payment else print(b)
print(b) if made_payment else print(a)