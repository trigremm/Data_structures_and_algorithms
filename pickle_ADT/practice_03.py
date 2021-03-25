"""
import ADT.Singly_Linked_List.pickle 
and count sum of all elements
"""

import os
import pickle
import sys

path = os.path.join("linked_lists", "circular_linked_list")
sys.path.insert(1, path)
from circular_linked_list import Circular_Linked_List as CLL

file = os.path.join('pickle_ADT', 'ADT.Circular_Linked_List.pickle')

with open(file, 'rb') as f:
    data = pickle.load(f)

### ADT usage
def get_name_and_print(data):
    print ('\n--- get_name_and_print ---')
    print (data.name)
    data.print()

def count_sum_of_1000_elements(data):
    print ('\n--- count_sum_of_1000_elements ---')
    s = 0
    node = data.head
    for _ in range(1000):
        s += node.data
        node = node.next
    print (s)

# homework
def add_negative_sum_to_tail(data):
    # task : Add -1 * sum of CLL value to the tail of CLL
    pass

if __name__ == '__main__':
    get_name_and_print(data)
    count_sum_of_1000_elements(data)
