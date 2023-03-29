class Node: 
    def __init__(self, key):
        self.data = key
        self.left_child = None
        self.right_child = None

class BSTDemo:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
        else:
            self._insert(self.root, key)

    # a private method in Python - a private method is meant for use within a class by other methods in the same class
    def _insert(self, curr, key):
        if key.data > curr.data: # if the node being inserted is greater than the root node
            if curr.right_child == None: # if there is no node on the right child of the root
                curr.right_child = key # the node goes to the right
            else: # if there is an existing right child
                self._insert(curr.right_child, key) # recursive function call with the existing right child as the root
        elif key.data < curr.data: 
            if curr.left_child == None: 
                curr.left_child = key
            else: 
                self._insert(curr.left_child, key) 
    

    def in_order(self):
        pass

    def _in_order(self, curr):
        pass

    def pre_order(self):
        pass

    def _pre_order(self, curr):
        pass

    def post_order(self):
        pass

    def _post_order(self, curr):
        pass

tree = BSTDemo()
tree.insert("F")
print(tree.root.data)
tree.insert("C")
print(tree.root.left_child.data)
tree.insert("G")
print(tree.root.right_child.data)
tree.insert("A")
print(tree.root.left_child.left_child.data)
tree.insert("B")
print(tree.root.left_child.left_child.right_child.data)
tree.insert("K")
print(tree.root.right_child.right_child.data)
tree.insert("H")
print(tree.root.right_child.right_child.left_child.data)