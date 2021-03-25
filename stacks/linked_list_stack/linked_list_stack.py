class Node:
    def __init__(self, data=None, next=None):
        self._data = data
        self._next = next

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next   

    @next.setter
    def next(self, next):
        self._next = next

class Linked_List_Stack:
    def __init__(self, data = None):
        self.name = 'Linked_List_Stack'
        self.head = None
        if data:
            self.push(data)
    
    def push(self, data = None):
        if data:
            new = Node(data, self.head)
            self.head = new

    def pop(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data
    
    def peek(self):
        if self.head is None:
            return None
        data = self.head.data
        return data

def main():
    my_stack = Linked_List_Stack()
    print('peek', my_stack.peek())
    print('pop', my_stack.pop())
    my_stack.push('111')
    my_stack.push('2')
    my_stack.push('33')
    my_stack.push('444')
    my_stack.push('55')
    my_stack.push('666')
    my_stack.peek()
    print('peek', my_stack.peek())
    print('pop', my_stack.pop())
    print('peek', my_stack.peek())
    print('pop', my_stack.pop())
    print('pop', my_stack.pop())
    print('pop', my_stack.pop())
    print('pop', my_stack.pop())
    print('pop', my_stack.pop())
    print('peek', my_stack.peek())
    my_stack.push('7')
    my_stack.push('88')
    print('peek', my_stack.peek())
    print('pop', my_stack.pop())
    print('pop', my_stack.pop())
    print('pop', my_stack.pop())

if __name__ == '__main__':
    main()