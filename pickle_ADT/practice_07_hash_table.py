"""
import ADT.HashTable.pickle 
and count number of words in table 
"""
### must have block 
import os
import pickle
import sys

# add class to import ADT
path = os.path.join("hash_table","")
sys.path.insert(1, path)
from hash_table import Hash_Table as HT

## deserialization - import ADT to program
file = os.path.join('pickle_ADT', 'ADT.Hash_Table.pickle')
with open(file, 'rb') as f:
    data = pickle.load(f)

# adt usage
def get_name_and_print(data):
    print ('\n--- get_name_and_print ---')
    print (data.name)
    

def inspect(ht):
    # inspect
    print (' --- inspect --- ' )
    for i_, i in enumerate(ht.slots):
        if i:
            print (i_, '::', i.key, '::', i.value)

def count_odd_values(sll):
    print ('\n--- count_odd_values ---')
    c = 0
    node = sll.head
    while node != None:
        if node.data % 2 == 1: # means it is odd
            c += 1
        node = node.next
    print ('number of odd values in the sll:', c)

def count_num_of_indexes(ht):
    _ = '\n\nfunction that counts number of obtained cells in ht'
    print (_)
    pass

def get_size_of_ht(ht):
    _ = '\n\nfunction to return size of ht'
    print (_)
    pass


if __name__ == '__main__':
    get_name_and_print(data)
    inspect(data)
    count_num_of_indexes(data)
    get_size_of_ht(data)
    
