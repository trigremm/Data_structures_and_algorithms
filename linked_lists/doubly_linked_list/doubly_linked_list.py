'''
doubly linked list implementation using Node 

author: askhat molkenov 
created: 20210217
edited: 20210317
'''

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
            
def init():
    print ('### init ###')
    
    ll = Doubly_Linked_List(5)
    for i in range(1, 4):
        j = (i+1)*5
        ll.insert(pos=i,data=j)
    
    ll.print()
    return ll

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

if __name__ == '__main__':
    main()
    # done