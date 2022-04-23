"""
import ADT.Singly_Linked_List.pickle 
and count sum of all elements
"""

import os
import pickle
import sys

from random import randint, seed

path = os.path.join("trees", "bst")
sys.path.insert(1, path)
from bst import Binary_Search_Tree as BST

def generate_BST(num=10, max=100, specific_number_flag=True):
    if specific_number_flag is False:
        num = randint(0, 2*num)
    data = BST()
    for _ in range(num):
        r = randint(1, max)
        data.insert(r)
    return data


def export_bst():
    data = generate_BST(specific_number_flag=False)
    file = os.path.join("pickle_ADT", "ADT.Binary_Search_Tree.pickle")
    with open(file, "wb") as handle:
        pickle.dump(data, handle)
    # print(f"{file=}")
    return file

def import_bst():
    file = os.path.join("pickle_ADT", "ADT.Binary_Search_Tree.pickle")
    with open(file, "rb") as f:
        data = pickle.load(f)
    # print(f"{data.name=}")
    return data

if __name__ == '__main__':
    data = import_bst()
    print(f"{data.name=}")
    data.print()
