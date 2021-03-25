class Node:
    def __init__(self,data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Node_Queue:
  def __init__(self):
    self.name = 'Node_Queue'
    self.head = None
    self.tail = None
    self.count = 0

  def enqueue(self, data):
    if (self.head == None):
      self.head = self.tail = Node(data)
    else:
        node = Node(data, None, self.tail)
        self.tail.next = node
        self.tail = node
    self.count += 1

  def dequeue(self):
    if self.count == 0:
      return None
    data = self.head.data
    if self.count == 1:
      self.head = None
      self.tail = None
    elif self.count > 1:
      self.head = self.head.next
      self.head.prev = None
    self.count -= 1
    return data

  def print (self):
    print ('count:', self.count, ', items:', end = ' ')
    node = self.head
    while node != None:
        print(node.data, end = ' ')
        node = node.next
    print ('')

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