class Stack(object):
    def __init__(self, limit = 10):
        self.stack = limit*[None]
        self.limit = limit
        self.index = 0

    def is_empty(self):
        return self.index <= 0
    
    def push(self, data):
        if self.index +1 >= self.limit:
            self.resize() 
        self.stack[self.index] = data
        self.index += 1

    def pop(self):
        if self.is_empty():
            print('[pop], Stack Underflow!')
            return None
        else:
            self.index -= 1
            return self.stack[self.index]
            
    def peek(self):
        if self.is_empty():
            print('[pop], Stack Underflow!')
            return None
        else:
            return self.stack[self.index-1]
    
    def size(self):
        return self.index
    
    def resize(self):
        self.limit = 2 * self.limit
        new_stack = [None] * self.limit
        for i_, i in enumerate(self.stack):
            new_stack[i_] = i
        self.stack = new_stack
    
    def pprint(self):
        print('pprint:', self.stack[:self.index])

    def true_print(self):
        print('true_print:', self.stack)        

def main():
    my_stack = Stack(5)
    print('peek', my_stack.peek())
    print('pop', my_stack.pop())
    my_stack.push('111')
    my_stack.push('2')
    my_stack.push('33')
    my_stack.push('444')
    my_stack.push('55')
    my_stack.push('666')
    my_stack.pprint()
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
    my_stack.pprint()
    my_stack.true_print()
    
if __name__ == '__main__':
    main()