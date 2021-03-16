'''
single linked list implementation using Node 

author: askhat molkenov 
created: 20210210
edited: 20210317
'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LL: # Linked List
    def __init__(self, data=None):
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

    def print(self): # traversing
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
        new.next = self.head # even if head is None it is Ok
        self.head = new

    def insert_at_end(self, data):
        new = Node(data)
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
        previous, current, i = self.head, self.head, 0
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
            
def insert_into_ll(ll):
    ll.print()

    d = 111
    p = 1
    print (f'insert data {d} into pos {p} # no change, ll empty, ')
    ll.insert(p, d); 
    ll.print()
    
    d = 222
    p = 0
    print (f'insert data {d} into pos {p} # begining')
    ll.insert(p, d)
    ll.print()

    d = 333
    p = ll.len() ; 
    print (f'insert data {d} into pos {p} # end');
    ll.insert(p, d)
    ll.print()
    
    for p in range(1, 5):
        d = 10**p
        print (f'insert data {d} into pos {p} # end');
        ll.insert(p, d)
        ll.print()

    return ll

def deletion_from_ll(ll):
    print ('delete first')
    ll.delete(0)
    ll.print ()

    print ('delete last')
    ll.delete(ll.len())
    ll.print ()

    print ('delete 2nd')
    ll.delete(2)
    ll.print ()

    print ('delete 2nd')
    ll.delete(2)
    ll.print ()
    return ll

def search (n, ll):
    ans = ll.search(n)
    ll.print()
    if ans == -1:
        print (f'{n} not in ll')
    else:
        print (f'{n} in ll at pos {ans}')

def search_in_ll(ll):
    print ('--- search in ')
    n = 5; search (n, ll)
    n = 10; search (n, ll)
    n = 100000; search (n, ll)

def over_deletion(ll):
    print ('delete 0th n times')
    for _ in range(ll.len() + 3):
        ll.print()
        ll.delete(0)
    return ll

def insert_into_empty_ll(ll):
    print ('--- insert_into_empty_ll ---')
    i, j = -2,1
    for _ in range(5):
        ll.insert(i,j)
        i, j = i+1, j*10
    ll.print ()

def main():
    ll = LL()

    insert_into_ll(ll)
    deletion_from_ll(ll)
    search_in_ll(ll)
    over_deletion(ll)
    insert_into_empty_ll(ll)

main()