class Node:

    def __init__(self, data=None):
        self.data = data # Node data
        self.next = None # Node pointer initially set to None since it doesn't point anything when created

    def __str__(self):
        return f"{self.data}" # return value of data

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self, x):
        '''add x to the end of the list'''
        if not isinstance(x, Node): # the 'isinstance' function in this case checks whether x is an instance of the Node class
            x = Node(x) # convert x to a Node
        if self.head == None:
            self.head = x # If list was empty, assign the first node as the head
        else:
            self.tail.next = x # If a node exists, assign a new node added to the list as the tail
        self.tail = x

    def __str__(self):
        to_print = ""
        curr = self.head
        while curr is not None:
            to_print += str(curr.data) + "->" # adding the string version of curr.data to to_print which is initially empty
            curr =  curr.next # going to the next element in the next iteration of the while loop
        if to_print:
            return "[" + to_print[:-2] + "]" # :-2 slices the last two elements from the returned string
        return "[]"

    def reverse_list_recur(self, current, previous):
        '''reverse the sequence of node pointers in the linked list'''
        # Given [1->2->3->4->5] reverse pointers [1<-2<-3<-4<-5] turning list to [5<-4<-3<-2<-1]

        if self.head == None: # if the list is empty
            return
        elif current.next == None: # when the tail is reached
            self.tail = self.head # tail points to the head
            current.next = previous # current node points to previous node
            self.head = current # set node as the new head
        else:
            next = current.next # e.g. 1 is currently pointing to 2 which is the next element
            current.next = previous # e.g. 1 no longer points to 2. Instead, 1 now points to None
            self.reverse_list_recur(next, current) # recursive function call now with 2 (the next element) as current and 1 as previous

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

my_list = LinkedList()
# print(my_list)

# my_list.append_val(node1)
# my_list.append_val(node2)
# my_list.append_val(node3)
# my_list.append_val(node4)
# my_list.append_val(5)
# print(my_list)

my_list.append_val(1)
my_list.append_val(2)
my_list.append_val(3)
my_list.append_val(4)
my_list.append_val(5)
print(my_list)
my_list.reverse_list_recur(my_list.head, None)
print(my_list)