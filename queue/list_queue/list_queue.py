class List_Queue:
    def __init__(self):
        self.name = 'List_Queue'
        self.items = []
        self.size = 0

    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        if self.items:
            data = self.items.pop()
            self.size -= 1
            return data
    
    def print(self):
        print('size:', self.size, 'items: ', end = ' ')
        for i in self.items:
            print (i, end=' ')
        print('\n')

def main():
    queue = List_Queue()
    print ('name:', queue.name)
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

if __name__ == '__main__':
    main()