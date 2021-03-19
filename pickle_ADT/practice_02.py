"""
import ADT.Doubly_Linked_List.pickle 
and count sum of squares all elements
"""

import os
import pickle
import sys

path = os.path.join("linked_lists", "doubly_linked_list")
sys.path.insert(1, path)
from doubly_linked_list import Doubly_Linked_List as DLL

file = os.path.join('pickle_ADT', 'ADT.Doubly_Linked_List.pickle')

with open(file, 'rb') as f:
    data = pickle.load(f)

print (data.name)
data.print()

s = 0
node = data.head
while node != None:
    s += node.data**2
    node = node.next
print (s)

# task : Find distance from max to min values in DLL

