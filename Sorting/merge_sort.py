# -*- coding: utf-8 -*-
# NAME: merge_sort.py

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
import random
from collections import deque
from datetime import datetime

# HELP FUNCTION SECTION
def merge(l1, l2):
    res_list = []
    l1 = deque(l1)
    l2 = deque(l2)

    while l1 and l2:
        if l1[0] < l2[0]:
            res_list.append(l1.popleft())
        else:
            res_list.append(l2.popleft())
    if not l1:
        res_list.extend(l2)
    if not l2:
        res_list.extend(l1)
    return res_list
#
# PRIMARY FUNCTION(S)
def merge_sort(list_of_items):
    """The list_of_items argument is expected to be a Python list.
    It is assumed the length of list_of_items is > 1."""

    ###############################################################
    #           INSERT YOUR MERGE SORT CODE HERE                  #
    ###############################################################
    if len(list_of_items) == 1:
        return list_of_items
    mid_idx = len(list_of_items) // 2
    sorted_left = merge_sort(list_of_items[:mid_idx])
    sorted_right = merge_sort(list_of_items[mid_idx:])
    list_of_items = merge(sorted_left, sorted_right)

    # Return the sorted list_of_items
    return list_of_items


#####################################################################################
if __name__ == "__main__":
    print("merge_sort.py : Is intended to be imported and not executed.")

    # Mayukh: just testing my merge sort code
    # l = list(range(1,100))
    # random.shuffle(l)
    # print(l)
    # print(merge_sort(l))


