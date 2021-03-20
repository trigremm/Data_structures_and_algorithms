'''
circular linked list implementation using Node 

author: askhat molkenov 
created: 20210219
edited: 20210316
'''

from random import randint

class Node:
    def __init__(self, data=None, next=None):
        self._data = data
        self._next = next

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next   

    @next.setter
    def next(self, next):
        self._next = next
    
class Circular_Linked_List:
    def __init__(self, data=None):
        self.name = 'Circular_Linked_List'
        self.head = None
        if data:
            self.insert_at_head(data)
    
    def insert_at_head(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new 
            new.next = self.head
            return
        node = self.head
        new.next = node
        while node.next != self.head: 
            node = node.next
        self.head = new
        node.next = self.head
        
    def insert_at_tail(self, data):
        new = Node(data)
        if self.head == None:
            return self.insert_at_head(data)
        node = self.head
        while node.next != self.head: 
            node = node.next
        node.next = new
        new.next = self.head
    
    def len(self):
        pass # homework

    def print(self): 
        node = self.head
        if node == None:
            return print ('CLL: empty\n')
        print ('CLL: ', end = '')
        print(node.data, end=' -> ')
        while node.next != self.head:
            node = node.next
            print(node.data, end=' -> ')
        print ('back_to_head\n')

    def delete_head(self):
        if self.head == None: 
            return 
        if self.head == self.head.next:
            self.head = None
            return
        current, second = self.head, self.head.next
        while current.next != self.head: 
            current = current.next
        self.head = second
        current.next = self.head

    def delete_tail(self):
        if self.head == None: 
            return
        if self.head == self.head.next:
            self.head = None
            return
        previous, current = self.head, self.head
        while current.next != self.head: 
            previous, current = current, current.next
        previous.next = self.head 

def example_insert_at_head():
    print(' +++ example_insert_at_head +++ ')
    ll = Circular_Linked_List()

    for i in 'head':
        ll.insert_at_head(i)
    ll.print()

def example_insert_at_tail():
    print(' +++ example_insert_at_tail +++ ')
    ll = Circular_Linked_List()

    for i in 'tail':
        ll.insert_at_tail(i)
    ll.print()

def example_delete_head():
    print(' --- example_delete_head --- ')
    ll = Circular_Linked_List()
    for ch in 'xyz':
        ll.insert_at_head(ch)
    ll.print ()

    while ll.head:
        ll.delete_head()
        ll.print ()

    for ch in 'head':
        ll.insert_at_tail(ch)
    ll.print ()

def example_delete_tail():
    print(' --- example_delete_tail --- ')
    ll = Circular_Linked_List()
    for ch in '12345':
        ll.insert_at_head(ch)
    ll.print ()

    while ll.head:
        ll.delete_tail()
        ll.print ()

    for ch in 'tail':
        ll.insert_at_tail(ch)
    ll.print ()

def main():
    example_insert_at_head()
    example_insert_at_tail()
    example_delete_head()
    example_delete_tail()
    
if __name__ == '__main__':
    main()