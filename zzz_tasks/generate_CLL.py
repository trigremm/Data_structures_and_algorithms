'''
generate random dataset and save it to pickle file

author: askhat molkenov 
edited: 20210316
'''

import os
path = os.path.join("linked_lists", "circular_linked_list")

import sys
sys.path.insert(1, path)

import pickle

from circular_linked_list import CLL
from random import randint

__default_filename__ = 'zzz_tasks/cll.pickle'

def generate_CLL():
    c = CLL()
    n = randint (10, 20)
    for _ in range(n):
        r = randint(1, 100)
        c.insert_into_tail(r)
    return c

def write_to_file(filename = __default_filename__, data = None):
    with open(filename, 'wb') as handle:
        pickle.dump(data, handle)

def main():
    c = generate_CLL()
    c.print()
    write_to_file(data = c)

if __name__ == '__main__':
    main()
