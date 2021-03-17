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

print (data.name)
data.print()

s = 0
node = data.head
for _ in range(1000):
    s += node.data
    node = node.next
print (s)


