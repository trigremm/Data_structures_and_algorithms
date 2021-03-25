"""
import ADT.Singly_Linked_List.pickle 
and count sum of all elements
"""
### must have block 
import os
import pickle
import sys

# add class to import ADT
path = os.path.join("linked_lists", "singly_linked_list")
sys.path.insert(1, path)
from singly_linked_list import Singly_Linked_List as SLL

## deserialization - import ADT to program
file = os.path.join('pickle_ADT', 'ADT.Singly_Linked_List.pickle')
with open(file, 'rb') as f:
    data = pickle.load(f)

# adt usage
def get_name_and_print(data):
    print ('\n--- get_name_and_print ---')
    print (data.name)
    data.print()

def count_sum(sll):
    print ('\n--- count_sum ---')
    s = 0
    node = sll.head
    while node != None:
        s += node.data
        node = node.next
    print (s)

def count_odd_values(sll):
    print ('\n--- count_odd_values ---')
    c = 0
    node = sll.head
    while node != None:
        if node.data % 2 == 1: # means it is odd
            c += 1
        node = node.next
    print ('number of odd values in the sll:', c)

if __name__ == '__main__':
    get_name_and_print(data)
    count_sum(data)
    count_odd_values(data)
