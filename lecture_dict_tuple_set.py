my_dictionary = {'name':'shaka', 'course':'python', 'fav_food': 'matumbo'}

phone_dict = {'shaka': '555-555-555',
              'zoolander': '999-99-9999',
              'jon snow': 'fail-o-so-bad'}

word_dict = {
              'a':
              {
                'apple': 'the round fruit of a tree of the rose family',
                'ant': 'an insect which cleans up the floor'
              },
              'b':
                 {
                  'bad': 'of poor quality of low standard',
                  'business': 'season 8 of GOT'
                 }
}

# Getting values in a dictionary
# print(word_dict['a'])
# print(word_dict['a']['ant'])
# print(word_dict['a']['ant'], word_dict['a']['apple'])

# print(my_dictionary.get('course'))

# # Adding a new key-value pair
# word_dict['c'] = 'car' 
# print(word_dict)

# # Updating an existng value
# my_dictionary['fav_food'] = 'biriani'
# print(my_dictionary)

# # Retrieving all the keys in a dictionary
# print(my_dictionary.keys())

# # Retrieving all the values in a dictionary
# print(my_dictionary.values())

# # Listing all the items in a dictionary
# print(my_dictionary.items()) 

# # When iterating through a dictionary using the for loop, you have to 
# # declare to variables i.e. one for the key and one for the value
# for k,v in my_dictionary.items():
#     print(k, v)


# Tuples
# Tuples are immutable and are created using parentheses
my_random_tuple = ('first',1,7,6,4,5,8,'hi there', 2,3,1,5,2,1,9,10)
# my_tuple = ('first_value', 'second_value', 'third_value')

# indexing in a tuple
# print(my_random_tuple[0])

# # displaying the tuple in a reversed order
# print(my_random_tuple[::-1])

# # Printing the methods available to a tuple
# print(dir(my_random_tuple))

# # Showing the number of elements in the tuple
# print(len(my_random_tuple))

# # Counting the number of occurences of a specific element
# print(my_random_tuple.count(5))

# # Finding the index associted with a certain element
# print(my_random_tuple.index('hi there'))

# # Unpacking values in a tuple
# my_tuple = ('first_value', 'second_value', 'third_value')
# first_var, second_var, third_var = my_tuple
# # print(second_var)

# # Using 'in' to find values in tuples. This returns a boolean value
# print('third_value' in my_tuple)

# # Iterating through a tuple
# for item in my_random_tuple:
#     print(item)


# Sets
# Sets are unordered collections of elements and because of this, you can't 
# index into any of the elements in a set
# You also cannot have duplicates in a set
# They are opened and closed using curly braces
# my_set = {1,6,2,'java','ruby',8,9,10,21,1000,'python'}
# print(my_set)

# # If you want to get rid of the duplicates in a list, you can cast it to 
# # a set
# my_list = [1,6,2,'java','ruby',8,9,10,21,1000,6,'python','java']
# print(my_list)
# my_set = set(my_list)# converting a list to a set
# print(my_set)

# # Finding information in a set. This returns a boolean value
# print('ruby' in my_set)

# # Mathematical operations in sets
my_set = {1,6,2,'java','ruby',8,9,10,21,1000,'python'}
# programming_set = {'java', 'ruby', 'javascript', 'python', 'c'}
# print(my_set.intersection(programming_set)) # displays the elements that are common between the two sets
# print(my_set.union(programming_set)) # all elements in the two sets put together, but without any duplicates
# print(my_set.difference(programming_set)) # all elements that exist in my_set that don't exist in programming_set
# print(programming_set.difference(my_set)) # all elements that exist in programmin_set that don't exist in my_set

# Iterating through a set
for item in my_set:
    print(item)