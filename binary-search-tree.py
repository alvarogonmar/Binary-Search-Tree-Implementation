class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.key == temp.key:
                return False
            if new_node.key < temp.key:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def search(self, key):
        temp = self.root
        while temp is not None:
            if key == temp.key:
                return True
            if key < temp.key:
                temp = temp.left
            else:
                temp = temp.right
