from random_generator import get_random_number, get_random_word


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Circular_Linked_List:
    def __init__(self, data=None):
        self.name = 'Circular_Linked_List'
        self.head = None
        if data:
            self.insert_into_head(data)

    def print(self):
        node = self.head
        if node == None:
            print('=== CLL is empty ===')
            return
        print('=== CLL ===')
        print(node.data, end=' -> ')
        while node.next != self.head:
            node = node.next
            print(node.data, end=' -> ')
        print('back_to_head\n')

    def insert_into_tail(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            self.head.next = new
            return
        node = self.head
        while node.next != self.head:
            node = node.next
        node.next = new
        new.next = self.head

    def insert_into_head(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            self.head.next = new
            return
        node = self.head
        new.next = node
        while node.next != self.head:
            node = node.next
        self.head = new
        node.next = self.head

    def delete_from_tail(self):
        if self.head == None:
            print('--- CLL is empty ---')
            return
        if self.head == self.head.next:
            self.head = None
            return
        previous = self.head
        current = self.head
        while current.next != self.head:
            previous, current = current, current.next
        previous.next = self.head

    def delete_from_head(self):
        if self.head == None:
            print('--- CLL is empty ---')
            return
        if self.head == self.head.next:
            self.head = None
            return
        second = self.head.next
        current = self.head
        while current.next != self.head:
            current = current.next
        self.head = second
        current.next = self.head


cll = Circular_Linked_List()
for i in range(get_random_number()):
    cll.insert_into_tail(get_random_word())

cll.print()

"""
task 1 
reverse words order in cll 

example: 
input:
q -> qw -> qwe -> qwer -> qwert -> NULL

output:
qwert -> qwer -> qwe -> qw -> q-> NULL
"""
# TYPE YOUR CODE HERE

