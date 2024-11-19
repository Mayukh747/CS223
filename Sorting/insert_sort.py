# -*- coding: utf-8 -*-
# NAME: insert_sort.py

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

# HELP FUNCTION SECTION


# PRIMARY FUNCTION(S)
def insert_sort(list_of_items):
    """The list_of_items argument is expected to be a Python list.
    It is assumed the length of list_of_items is > 1."""

    for j in range(1, len(list_of_items)):
        key = list_of_items[j]
        
        # Insert A[j] into the sorted sequence A[1, ..., j-1].
        i = j - 1
        while i >= 0 and list_of_items[i] > key:
            list_of_items[i+1] = list_of_items[i]
            i = i - 1
        list_of_items[i+1] = key

    # Return the sorted list_of_items
    return list_of_items


#####################################################################################
if __name__ == "__main__":
    print("insert_sort.py : Is intended to be imported and not executed.")


