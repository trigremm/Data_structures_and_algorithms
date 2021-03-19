"""
import ADT.Singly_Linked_List.pickle 
and count sum of all elements
"""

import os
import pickle
import sys

path = os.path.join("linked_lists", "singly_linked_list")
sys.path.insert(1, path)
from singly_linked_list import Singly_Linked_List as SLL


## deserialization
file = os.path.join('pickle_ADT', 'ADT.Singly_Linked_List.pickle')

with open(file, 'rb') as f:
    sll = pickle.load(f)

print (sll.name)
sll.print()

s = 0
node = sll.head
while node != None:
    s += node.data
    node = node.next
print (s)


c = 0
node = sll.head
while node != None:
    if node.data % 2 == 1: # means it is odd
        c += 1
    node = node.next
print ('number of odd values in the sll:', c)
