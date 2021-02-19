class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

class LL: # Linked List
    def __init__(self, data=None):
        if data:
            self.head = Node(data)
        else:
            self.head = None

    def size(self):
        n, c = self.head, 0 
        while n:
            n, c = n.get_next(), c+1
        return c

    def search(self, data):
        n, c = self.head, 0
        while n:
            if n.get_data() == data:
                return c
            n, c = n.get_next(), c+1
        return -1

    def print(self): # traversing
        if self.head == None:
            print('+++ SLL is empty +++')
            return
        print('+++ SLL +++')
        n = self.head
        while n != None:
            print(n.get_data(), end=' ')
            n = n.get_next()
        print('\n')

    def insert_at_beginig(self, data):
        new = Node(data)
        new.set_next(self.head) # even if head is None it is Ok
        self.head = new
        return

    def insert_at_middle(self, pos, data):
        node, i = self.head, 0
        while i != pos - 1: 
            node, i = node.get_next(), i+1
        new = Node(data)
        new.set_next(node.get_next())
        node.set_next(new)
        return

    def insert_at_end(self, data):
        node = self.head
        while node.get_next() != None:
            node = node.get_next()
        new = Node(data)
        node.set_next(new)

    def insert(self, pos, data):
        size = self.size()
        if pos < 0 or pos > size:
            return None
        if pos == 0:
            self.insert_at_beginig(data)
        elif pos == size:
            self.insert_at_end(data)
        else:
            self.insert_at_middle(pos, data)
            
    def delete_from_begining(self):
        self.head = self.head.get_next()

    def delete_from_end(self):
        previous, current = self.head, self.head
        while current.get_next() != None:
            previous, current = current, current.get_next()
        previous.set_next(None)

    def delete_from_middle(self, pos):
        previous, current, i = self.head, self.head, 0
        while i != pos - 1:
            previous, current, i = current, current.get_next(), i+1
        previous.set_next(current.get_next())

    def delete(self, pos):
        size = self.size()
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
    p = ll.size() ; 
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
    ll.delete(ll.size())
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
    for _ in range(ll.size() + 3):
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