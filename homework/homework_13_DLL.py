from random_generator import get_random_number, get_random_word

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next

class Doubly_Linked_List:
    def __init__(self, data = None):
        self.name = 'Doubly_Linked_List'
        self.head = self.tail = None
        if data:
            self.insert_into_head(data)

    def len(self):
        if self.head == None:
            return 0
        n, c = self.head, 0 
        while n:
            n, c = n.next, c+1
        return c

    def search(self, data):
        n, c = self.head, 0
        while n:
            if n.data == data:
                return c
            n, c = n.next, c+1
        return -1

    def print(self): # traversing
        print('--- DLL ---')
        n = self.head
        while n != None:
            print (n.data, end=' <=> ')
            n = n.next
        print('NULL\n')

    def insert(self, pos, data):
        if pos < 0 or pos > self.len():
            return None
        elif pos == 0:
            self.insert_into_head(data)
        elif pos == self.len():
            self.insert_into_tail(data)
        else:
            self.insert_into_middle(pos, data)

    def insert_into_head(self, data):
        new = Node(data)
        if self.head == None:
            self.head = self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        
    def insert_into_tail(self, data):
        new = Node(data)
        if self.head == None:
            self.head = self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new

    def insert_into_middle(self, pos, data):
        new = Node(data)
        n, p = self.head, 0
        while n and p < pos:
            n, p = n.next, p+1
        m = n.prev
        m.next = new
        new.prev = m
        new.next = n
        n.prev = new

    def delete(self, pos):
        if pos < 0 and pos >= self.len():
            return None
        if pos == 0:
            self.delete_head()
        elif pos == self.len()-1:
            self.delete_tail()
        else:
            self.delete_pos(pos)
            
    def delete_head(self):
        if self.head == None: # 0
            return
        elif self.head.next == None: # 1
            self.head = self.tail = None
        else: # more than 1
            next = self.head.next
            next.prev = None
            self.head.next = None
            self.head = next

    def delete_tail(self):
        prev = self.tail.prev
        self.tail.prev = None
        prev.next = None
        self.tail = prev
        
    def delete_pos(self, pos):
        n, p = self.head, 0
        while n and p < pos:
            n, p = n.next, p+1
        m, o = n.prev, n.next
        m.next = o
        o.prev = m
            
    def delete_value(self, value):
        while self.search(value) != -1: # doing search twice
            pos = self.search(value)    # doing search twice 
            self.delete(pos)

dll = Doubly_Linked_List()
for i in range(get_random_number()):
    dll.insert_into_tail(get_random_word())

dll.print()

"""
task 1 
sort words in dll by its lengts 

example: 
input:
delta <=> bob <=> charlie <=> dino <=> alpha <=> NULL

output:
bob <=> dino <=> delta <=> alpha <=> charlie <=> NULL
"""
# TYPE YOUR CODE HERE