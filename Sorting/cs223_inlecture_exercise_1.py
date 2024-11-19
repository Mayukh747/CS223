# -*- coding: utf-8 -*-
# NAME: cs223_inlecture_exercise_1.py

"""
AUTHOR: <your name>

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
import sys
import random
import math
from datetime import datetime
from copy import deepcopy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import insert_sort as iss
import selection_sort as ss
import quick_sort as qs
import merge_sort as ms

# CONSTANTS
_NUM_SAMPLES_TO_COLLECT_ = 10   # The number of timing samples to collect
_MIN_NUMBER_OF_NUMBERS_TO_GENERATE_ = 100   # Min number of random numbers to generate
_MAX_NUMBER_OF_NUMBERS_TO_GENERATE_ = 2300  # MAX number of random numbers to generate
_CURRENT_NUMBER_OF_NUMBERS_TO_GENERATE_ = _MIN_NUMBER_OF_NUMBERS_TO_GENERATE_    # Start generating min # nums
_NUMBER_TO_GENERATE_INCREMENT_ = \
    int((_MAX_NUMBER_OF_NUMBERS_TO_GENERATE_ - _MIN_NUMBER_OF_NUMBERS_TO_GENERATE_) / _NUM_SAMPLES_TO_COLLECT_)
_MIN_RANGE_NUM_ = 0     # The min number of the range of random numbers to generate
_MAX_RANGE_NUM_ = 1000      # The max number of the range of random numbers to generate
_NUM_SORT_TIMES_ = 3       # The number of time to call a sort algorithm ... to get an average sort time.
_RECURSION_LIMIT_ = 15000   # Max # time to recurse. Recursing an infinite # times will cause a stack overflow.
_AVG_TIME_ = 0.             # Average sort time

_PDF_COLUMN_NAMES_ = ['Size', 'Insert', 'Selection', 'Quick', 'Merge', 'n', 'nlg(n)', 'n^2']
# _COLS_TO_PLOT_ = ['Insert', 'Selection', 'Quick', 'Merge', 'n', 'nlg(n)', 'n^2']
_COLS_TO_PLOT_ = ['Insert', 'Selection', 'Quick', 'Merge', 'n', 'nlg(n)']


# HELP FUNCTION SECTION


# MAIN FUNCTION
def main():
    """The main inlectureram collects _NUM_SAMPLES_TO_COLLECT_ number of timing samples for
    InsertSort,  SelectionSort, and QuickSort (more sorting algorithms might be added later). The
    timing data is plotted for comparison purposes."""

    global _CURRENT_NUMBER_OF_NUMBERS_TO_GENERATE_
    global _COLS_TO_PLOT_

    # Create a Pandas DataFrame to hold timing data for each algorithm.
    # The "Size" column will specify the size of the list of items to be sorted.
    # The remaining columns will be labeled as "Insert", "Selection", and "Quick"
    # Each row will contain the average running time for an algorithm for the size of
    # the list of items as specified in the "Size" column on the same row.
    timing_data = pd.DataFrame(columns = _PDF_COLUMN_NAMES_,
                               index = [x for x in range(_NUM_SAMPLES_TO_COLLECT_)])

    print()
    print("##### STARTED TIMING InsertSort, SelectionSort, and QuickSort #####")

    for iteration in range(_NUM_SAMPLES_TO_COLLECT_ + 1):
        print()
        print("ITERATION: ", str(iteration))

        list_of_nums = []
        # Create a list of random numbers
        for i in range(_CURRENT_NUMBER_OF_NUMBERS_TO_GENERATE_):
            n = random.randint(_MIN_RANGE_NUM_, _MAX_RANGE_NUM_)     # Pick numbers between
            list_of_nums.append(n)

        saved_list_of_nums = deepcopy(list_of_nums)  
        nums_to_gen = "{:,}".format(_CURRENT_NUMBER_OF_NUMBERS_TO_GENERATE_)

        # Save size of list of items in Pandas dataFrame
        timing_data.at[iteration, 'Size'] = _CURRENT_NUMBER_OF_NUMBERS_TO_GENERATE_

        ##############################################################################
        # INSERT SORT
        iss_tot_time = 0.
        for i in range(_NUM_SORT_TIMES_):
            iss_start_time = datetime.now()
            res = iss.insert_sort(list_of_nums)
            iss_end_time = datetime.now()
            # print("Insert Sort Results: ", res)
            fmt = iss_end_time - iss_start_time
            iss_tot_time += float(fmt.total_seconds())

        iss_avg_time = iss_tot_time / _NUM_SORT_TIMES_
        msg = '  On average, InsertSort took {} secs to sort ' + str(nums_to_gen) + ' numbers.'
        print(msg.format(iss_avg_time))

        # Update Pandas dataframe timing_data
        timing_data.at[iteration, 'Insert'] = iss_avg_time 

        list_of_nums = deepcopy(saved_list_of_nums)
        ##############################################################################
        # SELECTION SORT
        ss_tot_time = 0.
        for i in range(_NUM_SORT_TIMES_):
            ss_start_time = datetime.now()
            res = ss.selection_sort(list_of_nums)
            ss_end_time = datetime.now()
            # print("Selection Sort Results: ", res)
            fmt = ss_end_time - ss_start_time
            ss_tot_time += float(fmt.total_seconds())

        ss_avg_time = ss_tot_time / _NUM_SORT_TIMES_
        msg = '  On average, SelectionSort took {} secs to sort ' + str(nums_to_gen) + ' numbers.'
        print(msg.format(ss_avg_time))

        # Update Pandas dataframe timing_data
        timing_data.at[iteration, 'Selection'] = ss_avg_time

        list_of_nums = deepcopy(saved_list_of_nums)
        ##############################################################################
        # QUICK SORT
        sys.setrecursionlimit(_RECURSION_LIMIT_)   # Set recursion limit for quick_sort
        qs_tot_time = 0.
        for i in range(_NUM_SORT_TIMES_):
            qs_start_time = datetime.now()
            res = qs.quick_sort(list_of_nums)
            qs_end_time = datetime.now()
            # print("Quick Sort Results: ", res)
            fmt = qs_end_time - qs_start_time
            qs_tot_time += float(fmt.total_seconds())

        qs_avg_time = (qs_tot_time / _NUM_SORT_TIMES_)
        msg = '  On average, QuickSort took {} secs to sort ' + str(nums_to_gen) + ' numbers.'
        print(msg.format(qs_avg_time))

        # Update Pandas dataframe timing_data
        timing_data.at[iteration, 'Quick'] = qs_avg_time / 2


        list_of_nums = deepcopy(saved_list_of_nums)
        ##############################################################################
        # MERGE SORT
        sys.setrecursionlimit(_RECURSION_LIMIT_)   # Set recursion limit for merge_sort
        ms_tot_time = 0.
        for i in range(_NUM_SORT_TIMES_):
            ms_start_time = datetime.now()
            res = ms.merge_sort(list_of_nums)
            ms_end_time = datetime.now()
            # print("Merge Sort Results: ", res)
            fmt = ms_end_time - ms_start_time
            ms_tot_time += float(fmt.total_seconds())

        ms_avg_time = (ms_tot_time / _NUM_SORT_TIMES_)
        msg = '  On average, MergeSort took {} secs to sort ' + str(nums_to_gen) + ' numbers.'
        print(msg.format(ms_avg_time))

        # Update Pandas dataframe timing_data
        timing_data.at[iteration, 'Merge'] = ms_avg_time

        ##############################################################################
        # Update 'n', 'nlg(n)', and 'n^2'  values in timing_data DataFrame to compare
        # with performance of sorting algorithms.
        if iteration == 0:
            _AVG_TIME_ = sum((timing_data.at[iteration, 'Insert'], timing_data.at[iteration, 'Selection'],
                        timing_data.at[iteration, 'Quick'])) / 3

        scale = iteration + 1
        n = _AVG_TIME_  * scale
        timing_data.at[iteration, 'n'] = n
        timing_data.at[iteration, 'nlg(n)'] = n * abs(math.log2(n))
        timing_data.at[iteration, 'n^2'] =  n * n
        ##############################################################################

        # Increment number of items to generate
        _CURRENT_NUMBER_OF_NUMBERS_TO_GENERATE_ += _NUMBER_TO_GENERATE_INCREMENT_

    print()
    print("Timing Data Table (in seconds):\n", timing_data)
    print()
    print("##### COMPLETED TIMING InsertSort, SelectionSort, QuickSort, MergeSort #####")
    print()
    print("##### PLOTTING TIMING DATA FOR InsertSort, SelectionSort, QuickSort, and MergeSort #####")
    plot_timing_data = timing_data[_COLS_TO_PLOT_]
    plot_timing_data.index = range(_MIN_NUMBER_OF_NUMBERS_TO_GENERATE_,
                                   _MAX_NUMBER_OF_NUMBERS_TO_GENERATE_ + _NUMBER_TO_GENERATE_INCREMENT_,
                                   _NUMBER_TO_GENERATE_INCREMENT_)
    p = sns.lineplot(data=plot_timing_data)
    p.set_xlabel('Number Of Items Sorted')
    p.set_ylabel('Time (Seconds)')
    print(plot_timing_data)
    plt.show()

    print()
    print("##### COMPLETED PLOTTING of TIMING DATA FOR InsertSort, SelectionSort, QuickSort, MergeSort #####")

    return


#####################################################################################
if __name__ == "__main__":
    main()
else:
    print("cs223_inlecture_exercise_1.py : Is intended to be executed and not imported.")
