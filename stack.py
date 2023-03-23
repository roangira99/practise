class Node:

    def __init__(self, data=None):
        '''initialize node with data and next pointer'''
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        '''initialize stack with stack pointer'''
        print("Stack created")
        self.stack_pointer = None # Tracking the head of the stack using the pointer

    def push(self, x):
        '''add x to the top of the stack'''
        if not isinstance(x, Node): # if new element is not a node,
            x = Node(x) # convert it to a node
        print(f"Adding {x.data} to the top of the stack")
        if self.is_empty(): # if the stack is empty
            self.stack_pointer = x # make the pointer point to the newly added node (x)
        else:
            x.next = self.stack_pointer
            self.stack_pointer = x

    def pop(self):
        '''remove and return the node on top of the stack'''
        if not self.is_empty(): # if the stack isn't empty
            print("Removing node on top of the stack")
            curr = self.stack_pointer # 'curr' is set to where the stack pointer is currently (which is the node at the top of the stack) and remains there
            self.stack_pointer = self.stack_pointer.next # the stack pointer moves/points to the next node 
            curr.next = None # pointer for the node at the top of the stack set to None, therefore delinking it from the rest of the stack
            return curr.data
        else:
            return "Stack is empty"
        
    def is_empty(self):
        '''return True if stack is empty, else return false'''
        return self.stack_pointer == None
    
    def peek(self):
        '''look at the node on top of the stack'''
        if not self.is_empty():
            return f"Checking item on top of stack: {self.stack_pointer.data}"
        
    def __str__(self):
        print("Printing Stack state...")
        to_print = ""
        curr = self.stack_pointer
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next
        if to_print:
            print("Stack Pointer")
            print(" |")
            print(" V")
            return "[" + to_print[:-2] + "]"
        return "[]"

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

my_stack = Stack()
print(f"Checking if stack is empty: {my_stack.is_empty()}")

my_stack.push(node1)
my_stack.push(node2)
print(my_stack)

my_stack.push(node3)
my_stack.push(node4)      
print(my_stack.peek())
my_stack.push(node5)      
print(my_stack)

print(my_stack.pop())
print(my_stack.pop())
print(my_stack)
my_stack.push(node4)      
print(my_stack)
        