class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self, data = None):
        self.head = None
        if data:
            self.push(data)
    
    def push(self, data = None):
        if data:
            temp = Node(data, self.head)
            self.head = temp
    def pop(self):
        if self.head is None:
            print ('[pop] stack underflow!')
            return 
        data = self.head.data
        self.head = self.head.next
        return data
    
    def peek(self):
        if self.head is None:
            print ('[peek] stack underflow!')
            return 
        data = self.head.data
        return data

def main():
    my_stack = Stack()
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