"""
import ADT.Singly_Linked_List.pickle 
and count sum of all elements
"""

import os
import pickle
import sys

path = os.path.join("queue", "node_queue")
sys.path.insert(1, path)
from node_queue import Node_Queue as SLL

file = os.path.join('pickle_ADT', 'ADT.Node_Queue.pickle')

with open(file, 'rb') as f:
    data = pickle.load(f)

print (data.name)
data.print()

s = 0
while data.count > 0:
    s += data.dequeue()
print (s)


