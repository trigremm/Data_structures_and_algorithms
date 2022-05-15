from random_generator import get_random_number, get_random_word

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linked_List_Stack:
    def __init__(self, data = None):
        self.name = 'Linked_List_Stack'
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



stack = Linked_List_Stack()
for i in range(get_random_number()):
    stack.push(get_random_word())

"""
task 1 
sort stack words by lengs in descending order

input:
a12
b123456
c123
d1234
e12345

output:
# print stack function 
b123456
e12345
d1234
c123
a12
"""
# TYPE YOUR CODE HERE


# print stack function 
while True:
    if stack.peek() is None:
        break
    item = stack.pop()
    print (item)