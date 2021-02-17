from random import randint
from statistics import mean

class profiler:
    def __init__(self):
        self.i = 0
    def inc(self):
        self.i += 1
    def show(self):
        return self.i
    def clear(self):
        self.i = 0

p = profiler()

def product_search(A, k):
    ''' A random integers array
    k randum integer 
    find m and n so that n*m == k'''
    for m in A:
        for n in A:
            p.inc()
            if m*n == k:
                p.inc()
                return m,n
    return None, None

def random_number(floor=0, ceil=100):
    return randint(floor, ceil)

def random_array(n=50, floor=0, ceil=100):
    return [randint(floor, ceil) for _ in range(n)]

an, af, ac = 50, 1, 100
kf, kc = 50, 1000

def main():
    a = random_array(an, af, ac)
    a = sorted(a)
    k = random_number(kf, kc)
    p.clear()

    m,n = product_search(a, k)
    return p.show()

def bins(): # new function that creates a dict where we will save our result 
    nruns = 10000
    arr = list()

    for _ in range(nruns):
        arr.append(main())
    print (mean(arr))

bins()
