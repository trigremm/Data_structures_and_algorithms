'''
bst - binary search tree

author: askhat molkenov 
created: 20210217
edited: 20210317
'''

from icecream import ic
from random import randint

class Node:
    def __init__(self, data):
        self._data = data
        self._right_child = None
        self._left_child = None
    
    def get_data(self): return self._data
    def get_right(self): return self._right_child
    def set_right(self, node): self._right_child = node
    def get_left(self): return self._left_child
    def set_left(self, node): self._left_child = node

class Tree:
    def __init__(self, data=None):
        self.root_node = None
        if data:
            self.insert(data)

    def find_min(self):
        current = self.root_node
        while current.get_left():
            current = current.get_left()
        return current

    def insert(self, data):
        new = Node(data)
        if self.root_node is None:
            self.root_node = new
            return 
        current, parent = self.root_node, None
        while True:
            parent = current
            if data < current.get_data():
                current = current.get_left()
                if current is None:
                    parent.set_left(new)
                    return
            else: 
                current = current.get_right()
                if current is None:
                    parent.set_right(new)
                    return
    
    def get_node_with_parent(self, data):
        current, parent = self.root_node, None
        while True:
            if current is None:
                return (parent, None)
            elif current.get_data() == data:
                return (parent, current)
            elif current.get_data() > data:
                current, parent = current.get_left(), current
            else:
                current, parent = current.get_right(), current

    def remove(self, data):
        parent, node = self.get_node_with_parent(data)
        
        if node is None:
            return False
        children_count = 0
        if node.get_left() and node.get_right():
            children_count = 2
        elif (node.get_left() is None) and (node.get_right() is None):
            children_count = 0
        else:
            children_count = 1
        if children_count == 0:
            if parent:
                if parent.get_right() is node:
                    parent.set_right(None)
                else:
                    parent.set_left(None)
            else:
                self.root_node = None
        elif children_count == 1:
            next_node = node.get_left() if node.get_left() else node.get_right()
            if parent:
                if parent.get_left() is node:
                    parent.set_left(next_node)
                else:
                    parent.set_right(next_node)
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.get_right()
            while leftmost_node.get_left():
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.get_left()
            node._data = leftmost_node.get_data() # please help me fix this line
            if parent_of_leftmost_node.get_left() == leftmost_node:
                parent_of_leftmost_node.set_left(leftmost_node.get_right())
            else:
                parent_of_leftmost_node.set_right(leftmost_node.get_right())

    def preorder(self, root_node):
        current = root_node
        if current is None:
            return
        print(current.get_data())
        self.preorder(current.get_left())
        self.preorder(current.get_right())
    
    def postorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.postorder(current.get_left())
        self.postorder(current.get_right())
        print(current.get_data())

    def print(self):
        print ('-'*40)
        self.print2D_node(self.root_node)
        print ('-'*40)

    def print2D_node(self, root, space = 0, TAB = 10) : 
        if (root == None) : 
            return
        space += TAB

        self.print2D_node(root.get_right(), space)

        print("\n", " " * (space - TAB), root.get_data())  

        self.print2D_node(root.get_left(), space) 

    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                return False
            elif current.get_data() == data:
                return True
            elif current.get_data() > data:
                current = current.get_left()
            else:
                current = current.get_right()


def nodes():
    n1 = Node("root_node")
    n2 = Node("left_child_node")
    n3 = Node("right_child_node")
    n4 = Node("left_grandchild_node")

    n1.set_left(n2)
    n1.set_right(n3)
    n2.set_left(n4)
    
    t = Tree()
    t.root_node = n1
    t.print()

def trees_example_1():
    t = Tree()
    t.insert(10)
    t.insert(5)
    t.insert(20)
    t.insert(10)
    t.insert(1)
    t.insert(7)
    t.insert(30)
    t.print()

    t.remove(30)
    t.print()

    if True:
        t.remove(20)
        t.print()

    t.remove(5)
    t.print()

    print ('tree search 1:', t.search(1))
    print ('tree search 2:', t.search(2))
    

def trees_example_2():
    t = Tree()
    for _ in range(10):
        r = randint(1, 100)
        t.insert(r)
    t.print()

def trees_example_3():
    print ('--- trees_example_3 ---')
    t = Tree()
    for data in [50,70,30,80,60, 40,20, 85,75,65,55,45,35,25,15]:
        t.insert(data)
    t.print()
    t.remove(50)
    t.print()
    t.remove(20)
    t.print()
    t.remove(10)
    t.print()
    t.remove(30)
    t.print()   
    print(t.root_node.get_data())
    print ('--- trees_example_3 --- end')

def main():
    nodes()
    trees_example_1()
    trees_example_2()
    trees_example_3()
    

if __name__ == '__main__':
    main()