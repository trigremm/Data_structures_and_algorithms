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
    
class CLL:
    def __init__(self, data=None):
        if data:
            self.head = Node(data)
            self.head.set_next(self.head)
        else:
            self.head = None
    
    def print(self): 
        node = self.head
        if node == None:
            print ('=== CLL is empty ===')
            return 
        print ('=== CLL ===')
        print(node.get_data(), end=' ') 
        node = node.get_next()
        while node != self.head:
            print(node.get_data(), end=' ')
            node = node.get_next()
        print ()
    
    def insert_into_tail(self, data):
        node = self.head
        new = Node(data)
        if self.head == None:
            self.head = new
            self.head.set_next(new)
            return
        while node.get_next() !=self.head: 
            node = node.get_next()
        node.set_next(new)
        new.set_next(self.head)

    def insert_into_head(self, data):
        node = self.head
        new = Node(data)
        if node == None:
            self.head = new
            self.head.set_next(new)
            return 
        new.set_next(node)
        while node.get_next() !=self.head: 
            node = node.get_next()
        self.head = new
        node.set_next(self.head)

    def delete_from_tail(self):
        if self.head == None: 
            print ('--- CLL is empty ---')
            return
        if self.head == self.head.get_next():
            self.head = None
            return
        previous = self.head
        current = self.head
        while current.get_next() != self.head: 
            previous = current;
            current = current.get_next()
        previous.set_next(self.head) 

    def delete_from_head(self):
        if self.head == None: 
            print ('--- CLL is empty ---')
            return 
        if self.head == self.head.get_next():
            self.head = None
            return
        second = self.head.get_next()
        current = self.head
        while current.get_next() != self.head: 
            current = current.get_next()
        self.head = second
        current.set_next(self.head)

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
        print (node.get_data(), end=' ')
        node = node.get_next()
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
    cll = CLL()
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