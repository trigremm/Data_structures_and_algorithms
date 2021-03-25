"""
import ADT.Doubly_Linked_List.pickle 
and count sum of squares all elements
"""

### must have block in order to import ADT from pickle file
import os
import pickle
import sys

path = os.path.join("linked_lists", "doubly_linked_list")
sys.path.insert(1, path)
from doubly_linked_list import Doubly_Linked_List as DLL

file = os.path.join('pickle_ADT', 'ADT.Doubly_Linked_List.pickle')

with open(file, 'rb') as f:
    data = pickle.load(f)

### ADT usage
def get_name_and_print(data):
    print ('\n--- get_name_and_print ---')
    print (data.name)
    data.print()

def count_sum_of_scuares(data):
    print ('\n--- count_sum_of_scuares ---')
    s = 0
    node = data.head
    while node != None:
        s += node.data**2
        node = node.next
    print (s)

# homework
def max_to_min_distance(data):
    # task : Find distance from max to min values in DLL
    pass

if __name__ == '__main__':
    get_name_and_print(data)
    count_sum_of_scuares(data)
