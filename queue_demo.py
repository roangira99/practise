class Node:

    def __init__(self, data=None):
        '''initialize node with data and next pointer'''
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        '''initiali queue with head and tail'''
        print("Queue created")
        self.head = None
        self.tail = None

    def add(self, x):
        '''append x to the tail of the queue'''
        if not isinstance(x, Node):
            x = Node(x)
        print(f"Appending {x.data} to the tail of the Queue")
        if self.is_empty():
            self.head = x
        else:
            self.tail.next = x
        self.tail =x
    
    def remove(self):
        '''remove and return the node at the head of the queue'''
        if not self.is_empty():
            print("Removing node at head of the Queue")
            curr = self.head # set the current node to be the head
            self.head = self.head.next # make the head to point to current.next
            curr.next = None # make current point to None
            return curr.data
        else:
            return "Queue is empty"
        
    def is_empty(self):
        '''return true if queue is empty, otherwise return false'''
        return self.head == None
    
    def peek(self):
        '''look at the node at head of the queue'''
        if not self.is_empty():
            return f"Checking node at the head of the queue: {self.head.data}"
        
    def __str__(self):
        print("Printing Queue state...")
        to_print = ""
        curr = self.head
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next
        if to_print:
            if len(to_print) > 4:
                print("Head", " "*(len(to_print)-9),"Tail")
                print(" |", " "*(len(to_print)-6), "|")
                print(" V", " "*(len(to_print)-6), "V")
                return "[" + to_print[:-2] + "]"
            else:
                print("Head and Tail")
                print(" |")
                print(" V")
                return "[" + to_print[:-2] + "]"
        return "[]"

my_queue = Queue()
print(f"Checking if Queue is empty: {my_queue.is_empty()}")
my_queue.add(1)
print(my_queue)
my_queue.add(2)
my_queue.add(3)
print(my_queue)
my_queue.add(4)
my_queue.add(5)
print(my_queue.peek())
my_queue.add(6)
print(my_queue)
print(my_queue.remove())
print(my_queue.remove())
print(my_queue)
my_queue.add(4)
print(my_queue)
