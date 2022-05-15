
class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Hash_Table:
    def __init__(self, size=256):
        self.name = 'Hash_Table'
        self.size = size
        self.slots = [None for _ in range(self.size)]
        self.count = 0

    def _hash(self, key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size
    
    def put(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        # seek for empty space
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h + 1) % self.size
        # dealing with collision
        if self.slots[h] is None:
            self.count += 1
        # asssignt value
        self.slots[h] = item

    def get(self, key):
        h = self._hash(key) 
        
        # check hash and get approrpiate value 
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h + 1) % self.size
        # if key is not in the ht - return None
        return None

def example_1():
    ht = Hash_Table()
    ht.put("good", "eggs")
    ht.put("better", "ham")
    ht.put("best", "spam")
    ht.put("ad", "do not")
    ht.put("ga", "collide")

    for key in ("good", "better", "best", "worst", "ad", "ga"):
        v = ht.get(key)
        print(v)

    # inspect
    print (' --- inspect --- ' )
    for i_, i in enumerate(ht.slots):
        if i:
            print (i_, i.key, i.value)

    for i in ht.slots:
        print (i, end = ' ')


if __name__ == '__main__':
    example_1()

# collision reslove solution : chaining 