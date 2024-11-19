# -*- coding: utf-8 -*-
# NAME: quick_sort.py

"""
AUTHOR: Leonard Wesley

  ============== VARIABLE, FUNCTION, etc. NAMING CONVENTIONS ==================
<ALL CAPITOL LETTERS>:  Indicates a symbol defined by a
        #define statement or a Macro.

   <Capitalized Word>:  Indicates a user defined global var, fun, or typedef.

   <all small letters>:  A variable or built in functions.


========================== MODIFICATION HISTORY ==============================
The format for each modification entry is:

MM/DD/YY:
    MOD:     <a description of what was done>
    AUTHOR:  <who made the mod>
    COMMENT: <any special notes to make about the mod (e.g., what other
              modules/code depends on the mod) >

    Each entry is separated by the following line:

====================== END OF MODIFICATION HISTORY ============================
"""

# IMPORTS
import os
from datetime import datetime
from typing import List


# HELP FUNCTION SECTION
def partition(list_of_items, p, r):
    x = list_of_items[r]
    i = p - 1

    for j in range(p, r):
        if list_of_items[j] <= x:
            i = i + 1
            temp = list_of_items[i]
            list_of_items[i] = list_of_items[j]
            list_of_items[j] = temp

    temp = list_of_items[i+1]
    list_of_items[i+1] = list_of_items[r]
    list_of_items[r] = temp

    return i + 1

def quick_sort2(list_of_items, p, r):
    # If p is < r, then there is more items to sort
    if p < r:
        q = partition(list_of_items, p, r)
        quick_sort2(list_of_items, p, q-1)
        quick_sort2(list_of_items, q+1, r)

    return list_of_items

# PRIMARY FUNCTION(S)
def quick_sort(list_of_items):
    """The list_of_items argument is expected to be a Python list.
    It is assumed the length of list_of_items is > 1."""

    # Call quick_sort2 with the proper arguments
    list_of_items = quick_sort2(list_of_items, 0, len(list_of_items)-1)

    # Return the sorted list_of_items
    return list_of_items


def linear_search(A: List[int], v: int):
    for idx in range(len(A)):
        if A[idx] == v:
            return idx
    return None

#####################################################################################
if __name__ == "__main__":
    print("insert_sort.py : Is intended to be imported and not executed.")



