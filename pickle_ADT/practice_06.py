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

file = os.path.join('pickle_ADT', 'ADT.Singly_Linked_List.pickle')

with open(file, 'rb') as f:
    data = pickle.load(f)

print (data.name)
data.print()

s = 0
node = data.head
while node != None:
    s += node.data
    node = node.next
print (s)


