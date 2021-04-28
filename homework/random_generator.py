import random

random.seed(0)

words = [line.strip() for line in open ("1000_random_words.txt")]

def get_random_word():
    return random.choice(words)

def get_random_number(a=10, b=20):
    return random.randint(a, b)

if __name__ == "__main__":
    for _ in range(10):
        print (get_random_word())
    for _ in range(10):
        print (get_random_number())
