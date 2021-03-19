"""
import ADT.Singly_Linked_List.pickle 
and count sum of all elements
"""

import os
import pickle
import sys

path = os.path.join("stacks", "linked_list_stack")
sys.path.insert(1, path)
from linked_list_stack import Linked_List_Stack as SLL

file = os.path.join('pickle_ADT', 'ADT.Linked_List_Stack.pickle')

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


