from random_generator import get_random_number, get_random_word


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Singly_Linked_List:
    def __init__(self, data=None):
        self.name = 'Singly_Linked_List'
        self.head = None
        if data:
            self.head = Node(data)

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

    def print(self):  # traversing
        if self.head == None:
            print('+++ SLL is empty +++')
            return
        print('+++ SLL +++')
        n = self.head
        while n != None:
            print(n.data, end=' -> ')
            n = n.next
        print('NULL\n')

    def insert_at_beginig(self, data):
        new = Node(data)
        new.next = self.head  # even if head is None it is Ok
        self.head = new

    def insert_at_end(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            return
        node = self.head
        while node.next != None:
            node = node.next
        node.next = new

    def insert_at_middle(self, pos, data):
        node, i = self.head, 0
        while i != pos - 1:
            node, i = node.next, i+1
        new = Node(data)
        new.next = node.next
        node.next = new

    def insert(self, pos, data):
        size = self.len()
        if pos < 0 or pos > size:
            return None
        if pos == 0:
            self.insert_at_beginig(data)
        elif pos == size:
            self.insert_at_end(data)
        else:
            self.insert_at_middle(pos, data)

    def delete_from_begining(self):
        self.head = self.head.next

    def delete_from_end(self):
        previous, current = self.head, self.head
        while current.next != None:
            previous, current = current, current.next
        previous.next = None

    def delete_from_middle(self, pos):
        previous, current, i = self.head, self.head, -1
        while i != pos - 1:
            previous, current, i = current, current.next, i+1
        previous.next = current.next

    def delete(self, pos):
        size = self.len()
        if pos < 0 or pos > size or size == 0:
            return None
        if pos == 0:
            self.delete_from_begining()
        elif pos == size:
            self.delete_from_end()
        else:
            self.delete_from_middle(pos)


sll = Singly_Linked_List()
for i in range(get_random_number()):
    sll.insert_at_end(get_random_word())

sll.print()

"""
task 1 
if word length in sll is even insert it's copy 

task 2
if word length in sll in odd delete it 

task 3
add to the begining lenght of changed sll  

example: 
input:
q -> qw -> qwe -> qwer -> qwert -> NULL

output:
4 -> qw -> qw -> qwer -> qwer -> NULL
"""


