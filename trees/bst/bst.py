'''
bst - binary search tree

author: askhat molkenov 
created: 20210217
edited: 20210317
'''

from icecream import ic
from random import randint

class Node:
    def __init__(self, data=None):
        self._data = data
        self._left = None
        self._right = None

    @property
    def data(self):
        return self._data

    @property
    def left(self):
        return self._left   

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right   

    @right.setter
    def right(self, right):
        self._right = right

class Binary_Search_Tree:
    def __init__(self, data=None):
        self.name = 'Binary_Search_Tree'
        self.root = None
        if data:
            self.insert(data)

    def find_min(self):
        current = self.root
        while current.left:
            current = current.left
        return current

    def insert(self, data):
        new = Node(data)
        if self.root is None:
            self.root = new
            return 
        current, parent = self.root, None
        while True:
            parent = current
            if data < current.data:
                current = current.left
                if current is None:
                    parent.left = new
                    return
            else: 
                current = current.right
                if current is None:
                    parent.right = new
                    return
    
    def get_node_with_parent(self, data):
        current, parent = self.root, None
        while True:
            if current is None:
                return (parent, None)
            elif current.data == data:
                return (parent, current)
            elif current.data > data:
                current, parent = current.left, current
            else:
                current, parent = current.right, current

    def remove(self, data):
        parent, node = self.get_node_with_parent(data)
        
        if node is None:
            return False
        children_count = 0
        if node.left and node.right:
            children_count = 2
        elif (node.left is None) and (node.right is None):
            children_count = 0
        else:
            children_count = 1
        if children_count == 0:
            if parent:
                if parent.right is node:
                    parent.right = None
                else:
                    parent.left = None
            else:
                self.root = None
        elif children_count == 1:
            next_node = node.left if node.left else node.right
            if parent:
                if parent.left is node:
                    parent.left = next_node
                else:
                    parent.right = next_node
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right
            while leftmost_node.left:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left
            node._data = leftmost_node.data # please help me fix this line
            if parent_of_leftmost_node.left == leftmost_node:
                parent_of_leftmost_node.left = leftmost_node.right
            else:
                parent_of_leftmost_node.right = leftmost_node.right

    def preorder(self, root):
        current = root
        if current is None:
            return
        print(current.data)
        self.preorder(current.left)
        self.preorder(current.right)
    
    def postorder(self, root):
        current = root
        if current is None:
            return
        self.postorder(current.left)
        self.postorder(current.right)
        print(current.data)

    def print(self):
        print ('-'*40)
        self.print2D_node(self.root)
        print ('-'*40)

    def print2D_node(self, root, space = 0, TAB = 10) : 
        if (root == None) : 
            return
        space += TAB

        self.print2D_node(root.right, space)

        print("\n", " " * (space - TAB), root.data)  

        self.print2D_node(root.left, space) 

    def search(self, data):
        current = self.root
        while True:
            if current is None:
                return False
            elif current.data == data:
                return True
            elif current.data > data:
                current = current.left
            else:
                current = current.right


def nodes():
    n1 = Node("root")
    n2 = Node("left_child_node")
    n3 = Node("right_child_node")
    n4 = Node("left_grandchild_node")

    n1.left = n2
    n1.right = n3
    n2.left = n4
    
    t = Binary_Search_Tree()
    t.root = n1 # not good to access element directly, better create setter 
    t.print()

def trees_example_1():
    t = Binary_Search_Tree()
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

    t.remove(20)
    t.print()

    t.remove(5)
    t.print()

    print ('tree search 1:', t.search(1))
    print ('tree search 2:', t.search(2))
    

def trees_example_2():
    t = Binary_Search_Tree()
    for _ in range(10):
        r = randint(1, 100)
        t.insert(r)
    t.print()

def trees_example_3():
    print ('--- trees_example_3 ---')
    t = Binary_Search_Tree()
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
    print(t.root.data)
    print ('--- trees_example_3 --- end')

def main():
    nodes()
    trees_example_1()
    trees_example_2()
    trees_example_3()
    

if __name__ == '__main__':
    main()