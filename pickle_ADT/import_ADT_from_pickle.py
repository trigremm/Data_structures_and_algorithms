import os
import pickle
import sys

path = os.path.join("linked_lists", "singly_linked_list")
sys.path.insert(1, path)
from singly_linked_list import Singly_Linked_List as SLL

file = 'ADT.Singly_Linked_List.pickle'

with open(file, 'rb') as f:
    data = pickle.load(f)

print (data.name)
data.print()

pos = data.search(77)
print (pos) 

data.delete(pos)
data.print()
