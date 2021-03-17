'''
circular linked list implementation using Node 

author: askhat molkenov 
created: 20210219
edited: 20210316
'''

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
            print ('=== CLL is empty ===')
            return 
        print ('=== CLL ===')
        print(node.data, end=' -> ') 
        while node.next != self.head:
            node = node.next
            print(node.data, end=' -> ')
        print ('back_to_head\n')
    
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
            print ('--- CLL is empty ---')
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
            print ('--- CLL is empty ---')
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

def try_to_insert_to_tail(cll):
    print ('--- try_to_insert_to_tail ---')
    for i in range(7):
        cll.insert_into_tail(i)
    cll.print()
    return cll
    
def try_to_insert_to_head(cll):
    print ('--- try_to_insert_to_head ---')
    for i in 'abc':
        cll.insert_into_head(i)
    cll.print()
    return cll

def check_if_it_circluar(cll):
    print ('--- check_if_it_circluar ---')
    node = cll.head
    for _ in range(30):
        print (node.data, end=' ')
        node = node.next
    print()
    return cll

def try_delete_from_head(cll):
    print ('--- try_delete_from_head ---')
    for _ in range(2):
        cll.delete_from_head()
        cll.print()
    return cll

def try_delete_from_tail(cll):
    print ('--- try_delete_from_tail ---')
    for _ in range(2):
        cll.delete_from_tail()
        cll.print()
    return cll

def overdelete_from_head(cll):
    print ('--- overdelete_from_head ---')
    for _ in range(10):
        cll.delete_from_head()
        cll.print()
    return cll

def overdelete_from_tail(cll):
    print ('--- overdelete_from_tail ---')
    for _ in range(10):
        cll.delete_from_tail()
        cll.print()
    return cll

def main():
    cll = Circular_Linked_List()
    print ('name:', cll.name)
    cll.print()
    cll = try_to_insert_to_tail(cll)
    cll = try_to_insert_to_head(cll)
    cll = check_if_it_circluar(cll)
    cll = try_delete_from_head(cll)
    cll = try_delete_from_tail(cll)
    cll = overdelete_from_head(cll)
    cll = try_to_insert_to_head(cll)
    cll = overdelete_from_tail(cll)
    
if __name__ == '__main__':
    main()