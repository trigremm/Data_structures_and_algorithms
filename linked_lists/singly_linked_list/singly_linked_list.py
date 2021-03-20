'''
single linked list implementation using Node 

author: askhat molkenov 
created: 20210210
edited: 20210317
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

class Singly_Linked_List:
    def __init__(self, data=None):
        self.name = 'Singly_Linked_List'
        self.head = None
        if data:
            self.insert_at_head(data)

    def insert_at_head(self, data):
        new = Node(data)
        new.next = self.head # even if head is None it is Ok
        self.head = new

    def insert_at_tail(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            return
        node = self.head
        while node.next != None:
            node = node.next
        node.next = new

    def insert_at_pos(self, pos, data):
        length = self.len()
        if pos < 0 or pos > length:
            return None
        elif pos == 0:
            return self.insert_at_head(data)
        elif pos == length:
            return self.insert_at_tail(data)
        new = Node(data)
        node, p = self.head, 0
        while node and p != pos - 1:
            node, p = node.next, p+1
        new.next = node.next
        node.next = new

    def len(self):
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
        if self.head == None:
            return print('SLL: empty\n')
        print('SLL: ', end='')
        n = self.head
        while n != None:
            print(n.data, end=' -> ' if n.next else '\n\n')
            n = n.next

    def delete_head(self):
        if self.head:
            self.head = self.head.next

    def delete_tail(self):
        length = self.len()
        if length <= 1:
            self.head = None
            return 
        previous, current = self.head, self.head
        while current.next != None:
            previous, current = current, current.next
        previous.next = None

    def delete_pos(self, pos):
        length = self.len()
        if pos < 0 or pos >= length:
            return None
        if pos == 0:
            return self.delete_head()
        if pos == length - 1:
            return self.delete_tail()
        previous, current, i = self.head, self.head, -1
        while i != pos - 1:
            previous, current, i = current, current.next, i+1
        previous.next = current.next

def example_insert_at_head():
    print(' +++ example_insert_at_head +++ ')
    ll = Singly_Linked_List()
    ll.print()

    for i in 'head':
        ll.insert_at_head(i)
    ll.insert_at_pos(-1, -11)
    ll.insert_at_pos(44, 44)
    ll.print()

def example_insert_at_tail():
    print(' +++ example_insert_at_tail +++ ')
    ll = Singly_Linked_List()
    ll.print()

    for i in 'tail':
        ll.insert_at_tail(i)
    ll.insert_at_pos(-1, -11)
    ll.insert_at_pos(44, 44)
    ll.print()

def example_insert_at_pos():
    print(' +++ example_insert_at_pos +++ ')
    ll = Singly_Linked_List()
    ll.print()

    for i in '1234567890':
        r = randint(0, ll.len())
        ll.insert_at_pos(r,i)
    ll.insert_at_pos(-1, -11)
    ll.insert_at_pos(44, 44)
    ll.print()

def example_delete_head():
    print(' --- example_delete_head --- ')
    ll = Singly_Linked_List()
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
    ll = Singly_Linked_List()
    for ch in '12345':
        ll.insert_at_head(ch)
    ll.print ()

    while ll.head:
        ll.delete_tail()
    ll.print ()

    for ch in 'tail':
        ll.insert_at_tail(ch)
    ll.print ()

def example_delete_pos():
    print(' --- example_delete_pos --- ')
    ll = Singly_Linked_List()
    for ch in '012345':
        ll.insert_at_tail(ch)
    ll.print()

    while ll.head:
        r = randint(0,ll.len()-1)
        print ('delete', r)
        ll.delete_pos(r)
        ll.print ()

    for ch in 'pos':
        ll.insert_at_pos(0, ch)
    ll.print ()

def search():
    print (' --- search --- ')
    ll = Singly_Linked_List()
    for i in '1234567890':
        ll.insert_at_pos(0,i)
    print (ll.search('5'))
    print (ll.search('0'))
    print (ll.search('a'))

def main():
    example_insert_at_head()
    example_insert_at_tail()
    example_insert_at_pos()
    example_delete_head()
    example_delete_tail()
    example_delete_pos()
    search()

if __name__ == '__main__':
    main()