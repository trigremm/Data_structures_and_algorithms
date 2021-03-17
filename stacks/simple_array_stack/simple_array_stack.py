class Simple_Array_Stack:
    def __init__(self, limit = 10):
        self.name = 'Simple_Array_Stack'
        self.stack = []
        self.limit = limit
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) >= self.limit

    def push(self, data):
        if self.is_full():
            print('[push] Stack Overflow!')
        else:
            self.stack.append(data)
    
    def pop(self):
        if self.is_empty():
            print('[pop]  Stack Underflow!')
            return None
        else:
            return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            print('[peek] Stack Underflow!')
            return None
        else:
            return self.stack[-1]
    
    def size(self):
        return len(self.stack)

def main():
    my_stack = Simple_Array_Stack(5)
    print('peek', my_stack.peek())
    print('pop', my_stack.pop())
    my_stack.push('111')
    my_stack.push('2')
    my_stack.push('33')
    my_stack.push('444')
    my_stack.push('55')
    my_stack.push('666')
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