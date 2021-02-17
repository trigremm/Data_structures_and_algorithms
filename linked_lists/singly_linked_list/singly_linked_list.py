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
    
    def has_next(self):
        return self.next != None

class LinkedList:
    def __init__(self, data=None):
        self.head = Node(data)
        self.size = 1
    
    def len(self):
        n, c = self.head, 0 
        while n:
            n,c = n.get_next(), c+1
        return c

    def search(self, data):
        n, c = self.head, 0
        while n:
            if n.get_data() == data:
                return c
            n, c = n.get_next(), c+1
        return -1

    def print(self): # traversing
        print('--- SLL ---')
        n = self.head
        while n != None:
            print (n.get_data(), end= ' ')
            n = n.get_next()
        print()

    def insert(self, pos, data):
        if pos < 0 or pos > self.size+1 or (pos > 0 and self.size == 0):
            return None
        if pos == 0:
            new = Node(data, self.head)
            self.head = new
            self.size += 1
        else:
            current = self.head
            count = 1
            while current.has_next(): 
                if count == pos:
                    new = Node(data, current.get_next())
                    current.set_next(new)
                    self.size += 1
                    return
                else:
                    current = current.get_next()
                count += 1
            if count <= pos : 
                new = Node(data, None)
                current.set_next(new)
                self.size += 1

    def delete(self, pos):
        if pos < 0 or pos > self.size:
            return None
        if self.size == 0:
            print("The linked list is empty")
            print('::', self.len())
            return
        if pos == 0:
            self.head = self.head.get_next()
            self.size -= 1
        else:
            prev, curr, i = self.head, self.head, 0
            while curr.has_next() and i < pos:
                prev, curr,i  = curr, curr.get_next(), i+1
            if curr.has_next():
                prev.set_next(curr.get_next())
                self.size -= 1
            else:
                prev.set_next(None)
                self.size -= 1

def init():
    i,j = 0,1
    ll = LinkedList(j)

    for _ in range(5):
        i, j = i+1, j*10
        ll.insert(i,j)
    
    ll.print()
    return ll

def insertion(ll):
    ll.print()

    d = 22; p = 2; print (f'insert data {d} into pos {p}');ll.insert(p, d); ll.print()
    
    d = 99; p = ll.len()+1; print (f'insert data {d} into pos {p}');ll.insert(p, d); ll.print()
    
    d = 555; p = 0; print (f'insert data {d} into pos {p}');ll.insert(p, d); ll.print()

    return ll

def deletion(ll):
    print ('delete last')
    ll.delete(ll.len())
    ll.print ()

    print ('delete 4th')
    ll.delete(4)
    ll.print ()

    print ('delete 0th')
    ll.delete(0)
    ll.print ()
    return ll

def search (n, ll):
    ans = ll.search(n)
    ll.print()
    if ans == -1:
        print (f'{n} not in ll')
    else:
        print (f'{n} in ll at pos {ans}')


def over_deletion(ll):
    print ('delete 0th n times')
    for _ in range(ll.size + 1):
        ll.print()
        ll.delete(0); print (ll.size)
    return ll

def insert_into_empty_ll(ll):
    i, j = -2,1
    for _ in range(5):
        ll.insert(i,j)
        i, j = i+1, j*10
    ll.print ()

def main():
    ll = init()
    
    ll = insertion(ll)

    ll = deletion(ll)

    n = 5; search (n, ll)
    n = 10; search (n, ll)
    n = 100000; search (n, ll)
    
    ll = over_deletion(ll)

    ll = insert_into_empty_ll(ll)

main()