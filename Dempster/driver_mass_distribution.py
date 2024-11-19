# - * - coding: utf - 8 -*-
"""
NAME: driver_mass_distribution.py

AUTHOR: Leonard P. Wesley

   Unpublished-rights reserved under the copyright laws of the United States.

   This data and information is proprietary to, and a valuable trade secret
   of, Leonard P. Wesley. It is given in confidence by Leonard
   P. Wesley. Its use, duplication, or disclosure is subject to
   the restrictions set forth in the License Agreement under which it has been
   distributed.

      Unpublished Copyright © 1992-2024  Leonard P. Wesley
      All Rights Reserved

  		This file is the driver for the mass_distribution.py module.

  ============== VARIABLE, FUNCTION, etc. NAMING CONVENTIONS ==================

  	<ALL CAPITOL LETTERS>:  Indicates a symbol defined by a #define
  					statement or a Macro.

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

  ----------

====================== END OF MODIFICATION HISTORY ============================

"""
from collections import defaultdict
from datetime import datetime
from typing import List, Set
import matplotlib.pyplot as plt
import seaborn as sns
import random
from itertools import chain, combinations
# IMPORTS
from mass_distribution import *


# MAIN FUNCTION
def main():
    prop1 = {'a', 'b'}
    prop2 = {'c', 'd'}

    prop_mass_pair1 = (prop1, 0.4)
    prop_mass_pair2 = (prop2, 0.6)

    mass_dist1 = [prop_mass_pair1, prop_mass_pair2]

    md1 = MassDistribution("mass_distribution_1")
    md1.set_mass_distribution(mass_dist1)

    print(md1.get_name()+":")
    print(md1.get_mass_distribution())
    print("Total mass of " + md1.get_name() + " is " + str(md1.get_mass()))


def powerset(s):
    """Generate all subsets of a set s."""
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))


def random_frame_of_discernment(theta, num_subsets=4):
    """Generate a random frame of discernment given a theta set."""

    # Generate powerset (excluding empty set)
    theta_powerset = powerset(theta)
    theta_powerset = [set(subset) for subset in theta_powerset if subset]  # convert tuples to sets

    # Randomly choose a number of subsets
    selected_subsets = random.sample(theta_powerset, num_subsets)

    # Generate random mass distribution (probabilities that sum to 1)
    random_probs = [random.random() for _ in range(num_subsets)]
    total = sum(random_probs)
    mass_dist = [p / total for p in random_probs]  # normalize to sum to 1

    # Create mass distribution as (subset, probability) tuples
    m1_mass_dist = list(zip(selected_subsets, mass_dist))
    # print(m1_mass_dist)

    md1 = MassDistribution("mass_distribution")
    md1.set_mass_distribution(m1_mass_dist)
    return md1


def generate_frame_list(theta: Set[str], list_length: int):
    """Given a proposition space and a length requirement, generate a list of frames"""
    frame_list = []

    for _ in range(list_length):
        frame_list.append(random_frame_of_discernment(theta))

    return frame_list


def dempster_rule(m1: MassDistribution, m2: MassDistribution) -> MassDistribution:
    '''Compute a consensus given two frames of discernment'''
    m3_prob_dist = defaultdict(float)
    k = 0

    md1 = m1.get_mass_distribution()
    md2 = m2.get_mass_distribution()

    for B in md1:
        for C in md2:
            A = B[0].intersection(C[0])
            # sets are not hashable, convert set to a sorted tuple
            A = tuple(x for x in sorted(A))

            if A:
                m3_A = B[1] * C[1]
                # print(B, C, A, m3_A)
                m3_prob_dist[A] += round(m3_A, 3)
                k += m3_A

    if k: # some orthogonal sums may have no intersections
        for A in m3_prob_dist:
            m3_prob_dist[A] = round(m3_prob_dist[A]/k,3)


    m3_mass_dist = [(set(A),m3_prob_dist[A]) for A in m3_prob_dist]

    md3 = MassDistribution("mass_distribution_result")
    md3.set_mass_distribution(m3_mass_dist)

    return md3


def dempster_rule_recurse(l: List[MassDistribution]) -> MassDistribution:
    """Divide and conquer recursive implementation of dempster's rule"""
    if len(l) == 1:
        return l[0]
    if len(l) == 2:
        return dempster_rule(l[0],l[1])
    else:
        mid_idx = len(l) // 2
        left = dempster_rule_recurse(l[:mid_idx])
        right = dempster_rule_recurse(l[mid_idx:])
        return dempster_rule(left, right)

def test_consensus_1():
    """Test the accuracy of dempster_rule"""
    mass_dist1 = [({'a'}, 0.2),
                  ({'a', 'b'}, 0.3),
                  ({'c'}, 0.2),
                  ({'a', 'b', 'c'}, 0.3),
                  ]

    md1 = MassDistribution("mass_distribution_1")
    md1.set_mass_distribution(mass_dist1)

    print(md1.get_name()+":")
    print(md1.get_mass_distribution())
    # print("Total mass of " + md1.get_name() + " is " + str(md1.get_mass()))

    mass_dist2 = [({'b'}, 0.3),
                  ({'b', 'c'}, 0.4),
                  ({'a', 'b', 'c'}, 0.3),
                  ]

    md2 = MassDistribution("mass_distribution_2")
    md2.set_mass_distribution(mass_dist2)

    print(md2.get_name()+":")
    print(md2.get_mass_distribution())
    # print("Total mass of " + md2.get_name() + " is " + str(md2.get_mass()))

    md3 = dempster_rule(md1, md2)

    print(md3.get_name() + ":")
    print(md3.get_mass_distribution())
    # print("Total mass of " + md3.get_name() + " is " + str(md3.get_mass()))

def test_consensus_2():
    """Test the accuracy of dempster_rule"""
    theta = {'A', 'C', 'F', 'P'}

    m1_mass_dist = [({'F', 'C'}, 0.48),
                    ({'A', 'F', 'C'}, 0.32),
                    ({'F', 'C', 'P'}, 0.12),
                    (theta, 0.08),
                    ]

    m2_mass_dist = [({'A'}, 0.9),
                    (theta, 0.1)]


    md1 = MassDistribution("mass_distribution_1")
    md1.set_mass_distribution(m1_mass_dist)

    print(md1.get_name()+":")
    print(md1.get_mass_distribution())
    # print("Total mass of " + md1.get_name() + " is " + str(md1.get_mass()))

    md2 = MassDistribution("mass_distribution_2")
    md2.set_mass_distribution(m2_mass_dist)

    print(md2.get_name()+":")
    print(md2.get_mass_distribution())
    # print("Total mass of " + md2.get_name() + " is " + str(md2.get_mass()))

    md3 = dempster_rule(md1, md2)

    print(md3.get_name() + ":")
    print(md3.get_mass_distribution())
    # print("Total mass of " + md3.get_name() + " is " + str(md3.get_mass()))

def plot_dempster_perf():
    """Collect data and plot the performance of dempster_rule_recurse"""
    dempster_perf = []
    #sample_dempster_perf = [0.000647, 0.006631, 0.07155, 0.164671, 0.18727, 0.246217, 0.305886, 0.39257, 0.420573, 0.48374, 0.543024, 0.601439]
    mass_dist_list_size = [10, 100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]


    theta = {'A', 'C', 'F', 'P'}
    m1_mass_dist = [({'F', 'C'}, 0.48),
                    ({'A', 'F', 'C'}, 0.32),
                    ({'F', 'C', 'P'}, 0.12),
                    (theta, 0.08),
                    ]
    md1 = MassDistribution("mass_distribution")
    md1.set_mass_distribution(m1_mass_dist)


    for size in mass_dist_list_size:

        MM_start_time = datetime.now()
        dempster_rule_recurse(generate_frame_list(theta, size))
        MM_stop_time = datetime.now()
        MM_time = float((MM_stop_time - MM_start_time).total_seconds())
        dempster_perf.append(MM_time)

    p = sns.lineplot(y=dempster_perf, x=mass_dist_list_size)
    p.set_title('recursive Dempster Rule runtime against # of Mass distributions')
    p.set_xlabel('# of Mass Distributions')
    p.set_ylabel('duration (seconds)')
    plt.show()

# Print imported/executed message
if __name__ == "__main__":
    print ("The driver_mass_distribution.py module has been successfully imported & executed.")
    # main()
    # plot_dempster_perf()
    mass_dist = [({'p2', 'p3'}, 0.2), ({'p4', 'p0'}, 0.65), ({'p4', 'p1', 'p0', 'p3'}, 0.04), ({'p4', 'p1'}, 0.04), ({'p3'}, 0.02),
     ({'p4', 'p1', 'p2', 'p3', 'p0'}, 0.05)]
    md1 = MassDistribution("mass_distribution")
    md1.set_mass_distribution(mass_dist)

else:
    print ("The driver_mass_distribution.py is not intended to be imported, only executed.")

#/////////////////////// END OF driver_mass_distribution.py FILE //////////////////////////