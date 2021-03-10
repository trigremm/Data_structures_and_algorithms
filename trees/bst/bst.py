'''
bst - binary search tree
'''
from icecream import ic
from random import randint

class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class Tree:
    def __init__(self):
        self.root_node = None

    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
            return 
        current = self.root_node
        parent = None
        while True:
            parent = current
            if node.data < current.data:
                current = current.left_child
                if current is None:
                    parent.left_child = node
                    return
            else: 
                current = current.right_child
                if current is None:
                    parent.right_child = node
                    return
    
    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        if current is None:
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child
        return parent, current

    def remove(self, data):
        parent, node = self.get_node_with_parent(data)
        if parent is None and node is None:
            return False
        children_count = 0
        if node.left_child and node.right_child:
            children_count = 2
        elif (node.left_child is None) and (node.right_child is None):
            children_count = 0
        else:
            children_count = 1
        if children_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root_node = None
        elif children_count == 1:
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child
            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
                self.root_node = next_node
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child
            node.data = leftmost_node.data
            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child

    def preorder(self, root_node):
        current = root_node
        if current is None:
            return
        print(current.data)
        self.preorder(current.left_child)
        self.preorder(current.right_child)
    def postorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.postorder(current.left_child)
        self.postorder(current.right_child)
        print(current.data)

    def print2D(self):
        print ('-'*40)
        self.print2D_node(self.root_node)
        print ('-'*40)

    def print2D_node(self, root, space = 0, TAB = 10) : 
        if (root == None) : 
            return
        space += TAB

        self.print2D_node(root.right_child, space)

        print("\n", " " * (space - TAB), root.data)  

        self.print2D_node(root.left_child, space) 

def nodes():
    n1 = Node("root node")
    n2 = Node("left child node")
    n3 = Node("right child node")
    n4 = Node("left grandchild node")

    n1.left_child = n2
    n1.right_child = n3
    n2.left_child = n4
    
    current = n1
    while current:
        print(current.data)
        current = current.left_child

def trees_example_1():
    t = Tree()
    t.insert(10)
    t.insert(5)
    t.insert(20)
    t.insert(10)
    t.insert(1)
    t.insert(7)
    print (t.root_node.data)
    print (t.root_node.left_child.data)
    print (t.root_node.left_child.left_child.data)
    print (t.root_node.left_child.right_child.data)
    t.remove(5)

    
    print (t.root_node.data)
    print (t.root_node.left_child.data)
    print (t.root_node.left_child.left_child.data)

def trees_example_2():
    t = Tree()
    for _ in range(10):
        r = randint(1, 100)
        t.insert(r)
    print ('preorder')
    t.preorder(t.root_node)
    print ('postorder')
    t.postorder(t.root_node)
    print ('---')
    print ('---')
    t.print2D()

def main():
    nodes()
    trees_example_1()
    trees_example_2()
    

if __name__ == '__main__':
    main()