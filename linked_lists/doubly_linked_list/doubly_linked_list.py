class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next

    def get_data(self):
        return self.data

    def get_prev(self):
        return self.prev

    def set_prev(self, prev):
        self.prev = prev

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

class DLL:
    def __init__(self, data=None):
        self.head = self.tail = Node(data)

    def len(self):
        if self.head == None:
            return 0
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
        print('--- DLL ---')
        n = self.head
        while n != None:
            print (n.get_data(), end= ' ')
            n = n.get_next()
        print()
        
    def insert_to_head(self, data):
        if (self.head == None):
            self.head = self.tail = Node(data)
        else:
            node = Node(data)
            node.set_next(self.head)
            self.head.set_prev(node)
            self.head = node
        
    def insert_to_tail(self, data):
        node = Node(data)
        self.tail.set_next(node)
        node.set_prev(self.tail)
        self.tail = node

    def insert(self, pos, data):
        if not (pos >=0 and pos <= self.len()):
            return None
        if pos == 0:
            self.insert_to_head(data)
        elif pos == self.len():
            self.insert_to_tail(data)
        else:
            n, p = self.head, 0
            while n and p < pos:
                n, p = n.get_next(), p+1
            node = Node(data)
            m = n.get_prev()
            m.set_next(node)
            node.set_prev(m)
            node.set_next(n)
            n.set_prev(node)

    def delete_head(self):
        if self.head.get_next() != None:
            next = self.head.get_next()
            next.set_prev(None)
            self.head.set_next(None)
            self.head = next
        else:
            self.head = self.tail = None

    def delete_tail(self):
        prev = self.tail.get_prev()
        self.tail.set_prev(None)
        prev.set_next(None)
        self.tail = prev
        
    def delete(self, pos):
        if not (pos >=0 and pos <= self.len()-1):
            return None
        if pos == 0:
            self.delete_head()
        elif pos == self.len()-1:
            self.delete_tail()
        else:
            n, p = self.head, 0
            while n and p < pos:
                n, p = n.get_next(), p+1
            m, o = n.get_prev(), n.get_next()
            m.set_next(o)
            o.set_prev(m)
            
    def delete_value(self, value):
        while self.search(value) != -1: # doing search twice
            pos = self.search(value)    # doing search twice 
            self.delete(pos)
            

def init():
    print ('### init ###')
    
    ll = DLL(5)
    for i in range(1, 4):
        j = (i+1)*5
        ll.insert(pos=i,data=j)
    
    ll.print()
    return ll

def get_node(ll):
    print ('### get_node ###')
    ll.print()
    n = 0; print (ll.get_node(n).get_data())
    n = 2; print (ll.get_node(n).get_data())
    n = ll.len(); print (ll.get_node(n).get_data())

def insertion(ll):
    print ('### insertion ###');ll.print()

    d = 26; p = 2; print (f'insert data {d} into pos {p}');
    ll.insert(p, d); ll.print()

    d = 66; p = 0; print (f'insert data {d} into pos {p}');
    ll.insert(p, d); ll.print()
    
    d = 99; p = ll.len(); print (f'insert data {d} into pos {p}');
    ll.insert(p, d); ll.print()
    return ll

def deletion(ll):
    print ('### deletion ###');ll.print ()

    print ('delete first'); ll.delete(0); ll.print ()

    print ('delete last'); ll.delete(ll.len()-1); ll.print ()
    
    print ('delete 3rd'); ll.delete(3); ll.print ()

    return ll

def search (ll):
    def search_one(n):
        ans = ll.search(n)
        if ans == -1:
            print (f'{n} not in ll')
        else:
            print (f'{n} in ll at pos {ans}')
    
    print ('### search ###')
    ll.print()
    n = 5; search_one (n)
    n = 15; search_one (n)
    n = 20; search_one (n)

def over_deletion(ll):
    print ('delete 0th n times')
    for _ in range(ll.len() + 1):
        ll.print()
        ll.delete(0); print (ll.len())
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

    search(ll)
    
    ll = over_deletion(ll)

    ll = insert_into_empty_ll(ll)

main()
# done