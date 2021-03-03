from random import randint, choice
pos = list(range(12))
c = choice(pos)
for _ in range(5):
    a, b, c = c, randint(1, 1000), choice(pos)
    print (a,b,c)
