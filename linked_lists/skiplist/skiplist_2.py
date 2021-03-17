'''
not functional yet ...

'''
from math import floor, log
from random import randint, seed

seed = 1000

class SkipNode:
    def __init__(self, data = None, height = 0):
        self.data = data
        self.next = [None]*height

class SkipList:
    def __init__(self, data=None, max_level=1):
        self.head = SkipNode(data, max_level)
        self.max_level = max_level

    def __len__(self):
        return self.len

    def random_level(self, max_level):
        num = randint(1, 2**max_level - 1) 
        lognum = log(num, 2)
        level = int(floor(lognum))
        return max_level - level

    def find(self, elem, update = None):
        if update == None:
            update = self.updateList(elem)
        if len(update) > 0:
            candidate = update[0].next[0]
            if candidate != None and candidate.elem == elem:
                return candidate
        return None
    
    def contains(self, elem, update = None):
        return self.find(elem, update) != None

    def randomHeight(self):
        height = 1
        while randint(1, 2) != 1:
            height += 1
        return height

    def updateList(self, elem):
        update = [None]*self.maxHeight
        x = self.head
        for i in reversed(range(self.maxHeight)):
            while x.next[i] != None and x.next[i].elem < elem:
                x = x.next[i]
            update[i] = x
        return update
        
    def insert(self, elem):

        node = SkipNode(self.randomHeight(), elem)

        self.maxHeight = max(self.maxHeight, len(node.next))
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)

        update = self.updateList(elem)            
        if self.find(elem, update) == None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
            self.len += 1

    def remove(self, elem):

        update = self.updateList(elem)
        x = self.find(elem, update)
        if x != None:
            for i in reversed(range(len(x.next))):
                update[i].next[i] = x.next[i]
                if self.head.next[i] == None:
                    self.maxHeight -= 1
            self.len -= 1            
                
    def printList(self):
        for i in range(len(self.head.next)-1, -1, -1):
            x = self.head
            while x.next[i] != None:
                print(x.next[i].elem,)
                x = x.next[i]
            print ('')