# Functions
# Functions are not tied to your object. Instead, you pass in your object 
# in the function
greeting = "hello"
user = "shaka"
message = "welcome to the Algorithms course"
# print(greeting, user, message)
# print(len(greeting))
# print(type(greeting))
# print(id(greeting)) # displays the memory location of an object
# print(id(user)) 

# Methods
# Unlike functions, methods are tied to the objects themselves by using the 
# dot operator to chain the method to the object
# print(greeting.upper(), user.capitalize(), message.strip().lower())
# We cn get a listing of some of the methods available to a particular class 
# of object by using the dir() funtion
# print(dir(greeting))
# print(message.find('the'))
# print(message.find('gw'))
# print(message.split())

# message2 = "Welcome-to-the-algorithms-course"
# print(message2.split("-")) #split based on the dashes

# my_languages = ['Python', 'Ruby', 'Javascript']
# print(" ".join(my_languages))
# print("-".join(my_languages))

# Importing modules
# import string 
# print(string.ascii_lowercase)
# OR
# from string import ascii_lowercase 
# print(ascii_lowercase)


# Formatting output and special characters
# Formatting output
# stock_price = "1100"
# print("Today's stock price for Netflix is:", stock_price)
# print("Today's stock price for Netflix is: {}".format(stock_price))
# print(f"Today's stock price for Netflix is: {stock_price}") # string interpolation
# print(f"Today's stock price for Netflix is: {4+5}") # string interpolation

# today_price = "1100"
# yesterday_price = "1000"
# print("Today's price: {}, yesterday's price: {}".format(today_price, yesterday_price))
# print(f"Today's price: {today_price}, yesterday's price: {yesterday_price}")

# Special characters
# Using the escape character (\) to break up long string
# print("My name is jon snow and\
# not only do I know nothing but\
# I also do nothing")

# The new line character (\n) enables the output of 
# a string to be split into multiple lines
# print("My name is jon snow\nI know nothing\nI also do nothing")

# The tab character adds tabs to the string
# print("My name is jon snow\n\tI know nothing\n\t\tI also do nothing")

# If you want to show the special character you are using add a backslash before it:
print("I'm using the \\n special character to create new lines")
