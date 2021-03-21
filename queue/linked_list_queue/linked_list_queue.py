'''
node queue implementation using Node 

author: askhat molkenov 
created: 20210320
'''

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self._data = data
        self._next = next
        self._prev = prev

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next   

    @next.setter
    def next(self, next):
        self._next = next

    @property
    def prev(self):
        return self._prev   

    @prev.setter
    def prev(self, prev):
        self._prev = prev

class Node_Queue:
    def __init__(self, data = None):
        self.name = 'Linked_List_Queue'
        self.head, self.tail, self.count = None, None, 0
        if data:
            self.enqueue(data)

    def enqueue(self, data):
        new = Node(data)
        if self.head == None:
            self.head = self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            return None
        data = self.head.data
        if self.count == 1:
            self.head, self.tail = None, None
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None
        self.count -= 1
        return data

    def print (self):
        print ('count:', self.count, ', queue:', end = ' ')
        node = self.head
        while node != None:
            print(node.data, end = ' <- ' if node.next else '')
            node = node.next
        print ('\n')

def main():
    queue = Node_Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.print()
    _ = queue.dequeue()
    queue.print()
    _ = queue.dequeue()
    _ = queue.dequeue()
    _ = queue.dequeue()
    _ = queue.dequeue()
    queue.print()    
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)    
    queue.print()
    print (queue.name)

if __name__ == '__main__':
    main()