'''
generate random dataset and save it to pickle file

author: askhat molkenov 
edited: 20210316
'''

import os
import pickle
import sys

from random import randint, seed

seed(20210316)

path = os.path.join("linked_lists", "singly_linked_list")
sys.path.insert(1, path)
from singly_linked_list import Singly_Linked_List as SLL

def generate_SLL():
    data, n = SLL(), randint (10, 20)
    for _ in range(n):
        r = randint(1, 100)
        data.insert_at_end(r)
    return data
    
path = os.path.join("linked_lists", "circular_linked_list")
sys.path.insert(1, path)
from circular_linked_list import Circular_Linked_List as CLL

def generate_CLL():
    data, n = CLL(), randint (10, 20)
    for _ in range(n):
        r = randint(1, 100)
        data.insert_into_tail(r)
    return data

path = os.path.join("linked_lists", "doubly_linked_list")
sys.path.insert(1, path)
from doubly_linked_list import Doubly_Linked_List as DLL

def generate_DLL():
    data, n = DLL(), randint (10, 20)
    for _ in range(n):
        r = randint(1, 100)
        data.insert_into_tail(r)
    return data

path = os.path.join("queue", "node_queue")
sys.path.insert(1, path)
from node_queue import Node_Queue as NQ

def generate_NQ():
    data, n = NQ(), randint (10, 20)
    for _ in range(n):
        r = randint(1, 100)
        data.enqueue(r)
    return data

path = os.path.join("stacks", "linked_list_stack")
sys.path.insert(1, path)
from linked_list_stack import Linked_List_Stack as LLS

def generate_LLS():
    data, n = LLS(), randint (10, 20)
    for _ in range(n):
        r = randint(1, 100)
        data.push(r)
    return data

path = os.path.join("trees", "bst")
sys.path.insert(1, path)
from bst import Binary_Search_Tree as BST

def generate_BST():
    data, n = BST(), randint (10, 20)
    for _ in range(n):
        r = randint(1, 100)
        data.insert(r)
    return data

path = os.path.join("hash_table", "")
sys.path.insert(1, path)
from hash_table import Hash_Table as HT

def generate_HT():
    text = """
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
    data = HT(32)
    for line in text.split('\n'):
        if line.strip():
            arr = line.split(' ')
            for i in arr:
                if data.get(i) == None:
                    print (i, line)
                    data.put(i, line)
                    break
    return data

def write_to_file(data = None):
    if data is None:
        return
    out = os.path.join('ADT.' + data.name + '.pickle')
    with open(out, 'wb') as handle:
        pickle.dump(data, handle)
    print (out, '\n')

def main():
    data = generate_CLL()
    data.print()
    write_to_file(data = data)

    data = generate_DLL()
    data.print()
    write_to_file(data = data)

    data = generate_SLL()
    data.print()
    write_to_file(data = data)

    data = generate_NQ()
    data.print()
    write_to_file(data = data)

    data = generate_LLS()
    print ('name:', data.name)
    write_to_file(data = data)

    data = generate_BST()
    data.print()
    write_to_file(data = data)

    data = generate_HT()
    write_to_file(data = data)

if __name__ == '__main__':
    main()
