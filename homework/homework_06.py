from random_generator import get_random_number, get_random_word


class PriorityQueue(object):
    def __init__(self, levels):
        self.queue = dict()
        self.n = levels
        for i in range(levels):
            self.queue[i] = []

    def print(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, data, level=None):
        if level == None:
            level = self.n - 1
        self.queue[level].append(data)

    def dequeue(self):
        for i in range(self.n):
            if self.queue[i]:
                a = self.queue[i][0]
                self.queue[i] = self.queue[i][1:]
                return i, a
        else:
            return None, None


levels = get_random_number(3, 6)
myQueue = PriorityQueue(levels)
for i in range(get_random_number()):
    random_level = get_random_number(0, levels-1)
    random_word = get_random_word()
    myQueue.enqueue(random_word, random_level)


"""
task 1 
for each queue 
if consonant number is odd put word to higher queue 
if consonant number is even put word to lower queue 

example: 
input:
0 b1 cc2 ddd3 ffff4 
1 l1 mm2 ppp3 qqqq4
2 r1 ss2 ttt3 wwww4

output:
0 b1 ddd3 l1 ppp3
1 cc2 ffff4 r1 ttt3
2 ss2 wwww4 mm2 qqqq4 
"""
# TYPE YOUR CODE HERE


# queue print function
while True:
    level, word = myQueue.dequeue()
    if level == None:
        break
    print(level, word)
