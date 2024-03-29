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
        if key.data > curr.data:  # if the node being inserted is greater than the root node
            if curr.right_child == None:  # if there is no node on the right child of the root
                curr.right_child = key  # the node goes to the right
            else:  # if there is an existing right child
                self._insert(curr.right_child, key)  # recursive function call with the existing right child as the root
        elif key.data < curr.data:
            if curr.left_child == None:
                curr.left_child = key
            else:
                self._insert(curr.left_child, key)

    def in_order(self):
        # left, root, right
        self._in_order(self.root)
        print("")

    def _in_order(self, curr):
        if curr:
            self._in_order(curr.left_child)
            print(curr.data, end=" ")
            self._in_order(curr.right_child)

    def pre_order(self):
        '''root, left, right'''
        self._pre_order(self.root)
        print("")

    def _pre_order(self, curr):
        if curr:
            print(curr.data, end=" ")
            self._pre_order(curr.left_child)
            self._pre_order(curr.right_child)

    def post_order(self):
        '''left, right, root'''
        self._post_order(self.root)
        print("")

    def _post_order(self, curr):
        if curr:
            self._pre_order(curr.left_child)
            self._pre_order(curr.right_child)
            print(curr.data, end=" ")

    # search for a value in the tree
    def find_val(self, key):
        return self._find_val(self.root, key)  # Kick off the search with the root node

    def _find_val(self, curr, key):
        if curr:
            if key == curr.data:
                return "Value found in tree"
            elif key < curr.data:
                return self._find_val(curr.left_child, key)
            else:
                return self._find_val(curr.right_child, key)
        return "Value not found in tree"

    def min_right_subtree(self, curr):
        if curr.left_child == None:
            return curr
        else:
            return self.min_right_subtree(curr.left_child)

    def delete_val(self, key):
        self._delete_val(self.root, None, None, key)

    def _delete_val(self, curr, prev, is_left, key):
        if curr:
            if key == curr.data:
                # For deleting a node with both left and right child
                if curr.left_child and curr.right_child:
                    min_child = self.min_right_subtree(curr.right_child)  # Obtaining the minimum node in the right subtree
                    curr.data = min_child.data # copying over the data of the min child to the parent node
                    self._delete_val(curr.right_child, curr, False, min_child.data)  # removing the duplicate node on the right subtree which we initially copied from
                # For deleting a node with no children
                elif curr.left_child == None and curr.right_child == None:
                    if prev:
                        if is_left:  # If current node is the left child
                            prev.left_child = None  # set parent pointer to None
                        else:
                            prev.right_child = None
                    else:
                        self.root = None
                elif curr.left_child == None:  # check if the current node (F) has no left child
                    if prev:  # If previous exists / if not root node
                        if is_left:  # check if the current node is the left child of the previous node
                            prev.left_child = curr.right_child  # make the previous node point to the current node's
                            # right child
                        else:  # check if the current node is the right child of the previous node
                            prev.right_child = curr.right_child
                    else:  # if root node
                        self.root = curr.right_child  # copy value of the right child to root
                else:
                    if prev:
                        if is_left:  # check if the current node is the left child of the previous node
                            prev.left_child = curr.left_child  # make the previous node point to the current node's
                            # left child
                        else:  # check if the current node is the right child of the previous node
                            prev.right_child = curr.left_child
                    else:  # if root node
                        self.root = curr.left_child  # copy value of the left child to root

            elif key < curr.data:
                self._delete_val(curr.left_child, curr, True, key)
            elif key > curr.data:
                self._delete_val(curr.right_child, curr, False, key)
        else:
            print(f"{key} not found in tree")


tree = BSTDemo()

# tree.insert("C")
# tree.in_order()
# tree.delete_val("F")
# tree.in_order()

tree.insert("F")
tree.insert("C")
# print(tree.root.data)
# print(tree.root.left_child.data)
tree.insert("G")
# print(tree.root.right_child.data)
tree.insert("A")
# print(tree.root.left_child.left_child.data)
tree.insert("B")
# print(tree.root.left_child.left_child.right_child.data)
tree.insert("K")
# print(tree.root.right_child.right_child.data)
tree.insert("H")
# print(tree.root.right_child.right_child.left_child.data)
tree.insert("E")
tree.insert("D")
tree.insert("I")
tree.insert("M")
tree.insert("J")
tree.insert("L")
tree.in_order()
tree.delete_val("F")
tree.in_order()
tree.in_order()
tree.delete_val("K")
tree.in_order()
tree.in_order()
tree.delete_val("C")
tree.in_order()
tree.delete_val("Y")

# tree.in_order()
# tree.pre_order()
# tree.post_order()
# print(tree.find_val("C"))


# We need to know the parent of the node we want to remove
# We need to determine whether the node we want to remove is the
# left child or the right child