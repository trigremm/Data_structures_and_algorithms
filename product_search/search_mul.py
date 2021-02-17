from random import randint

def product_search(A, k):
    ''' A random integers array
    k randum integer 
    find m and n so that n*m == k'''
    for m in A:
        for n in A:
            if m*n == k:
                return m,n
    return None, None

def random_number(floor=0, ceil=100):
    return randint(floor, ceil)

def random_array(n=50, floor=0, ceil=100):
    return [randint(floor, ceil) for _ in range(n)]
    
def main():
    an, af, ac = 50, 1, 100
    kf, kc = 50, 1000

    a = random_array(an, af, ac)
    k = random_number(kf, kc)

    m,n = product_search(a, k)
    print (f"{k} = {m}*{n};\n{m}, {n} from {a}")

main()
