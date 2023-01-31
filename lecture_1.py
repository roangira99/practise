# print('Hello world using single quotes')
# print("Hello world using double quotes")
# print("""Hello world using triple quotes,
# also known as multi-line strings""")

# print("Hello world I'm using an apostrophe")
# print('Hello world "using quotes here" double quotes within the string.')

# # Using an escape character
# print('Hello world I\'m using an apostrophe')
# print("Hello world \"using quotes here\" double quotes within the string.")

# Variables
# my_message = 'Hello world I\'m using single quotes'
# print(my_message)

# Concatenation
message = "The price of the stock is:"
print(id(message))

price = "$100"
# new_message = message + " " + price
# print(new_message)
message = message + price # new variable with the same name but it is a different object from the previous one
# print(message)
print(id(message))

# NB: Strings are immutable, therefore you cannot change them once they are declared
# you can only modify it by re-assigning the variable as shown above

# Slicing - The stop index is not included in the slice

