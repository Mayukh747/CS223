# - * - coding: utf - 8 -*-
"""
NAME: mass_distribution.py

AUTHOR: Leonard P. Wesley

   Unpublished-rights reserved under the copyright laws of the United States.

   This data and information is proprietary to, and a valuable trade secret
   of, Leonard P. Wesley. It is given in confidence by Leonard
   P. Wesley. Its use, duplication, or disclosure is subject to
   the restrictions set forth in the License Agreement under which it has been 
   distributed.

      Unpublished Copyright © 1992-2024  Leonard P. Wesley
      All Rights Reserved

  		This file includes the base class definitions for evidential mass
  		distributions as well as the types of propositions.

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

# IMPORTS
from copy import deepcopy

"""
The structure of a discrete mass distribution is a list of tupples where each tuple 
is a prop-mass-pair. HOWEVER, some definitions first.

DISCRETE PROPOSITION:  a python string, e.g., 'a'  is a proposition, 'hot' is another 
      example of a proposition, 'cold' is another example, 'cc' is yet another example. 
      
SET OF DISJOINT AND MUTUALLY EXCLUSIVE DISCRETE PROPOSITIONS:  a set of one or more DISCRETE 
      PROPOSITIONS. For example,  {'a'} is a set of one disjoint and mutually exclusive 
      propositions.  {'hot', 'b'} is another example of a set of disjoint and mutually 
      exclusive propositions, and {'cold', 'hot', 'cc'} is yet another example of a set of 
      disjoint and mutually exclusive propositions.  

A MASS VALUE: a floating point number > 0 and <= 1.  For example, 0.5 is a mass value, 0.254 is 
        another mass value, ...etc. 
        
PROP MASS PAIR:  a tuple of a set of disjoint and mutually exclusive propositions and a 
      mass value. For example, ({'hot', 'b'}, 0.5) is an example of a PROP MASS PAIR. 
      ({'a', 'b', 'c'}, 0.334) is another example of a PROP MASS PAIR. 
      
MASS DISTRIBUTION: a Python list consisting of one or more PROP MASS PAIRs such that the sum of the mass associated with
    each PROP MASS PAIR  sums to 1.0.  For example [ ({'a', 'b', 'c'}, 0.334), ({'hot', 'b'}, 0.5), 
    ({'cold', 'medium'}, 0.166) ]  

TRUE PROPOSITION: a set of mutually exclusive and exhaustive propositions that represents
     all possible outcomes/observations assiated with a random variable called a frame (within
     the context of belief functions and evidential reasoning. For example, {'a', 'b', 'c'} is 
     an example of a true proposition.  

"""
class MassDistribution:
    # Class index for MassDistribution class
    __MASSDISTRIBUTION_INDEX__ = 1

    # Constructor
    def __init__(self, name=None, true_prop=None):
        if name == None:
            self.name = 'md_' + str(MassDistribution.__MASSDISTRIBUTION_INDEX__)
            MassDistribution.__MASSDISTRIBUTION_INDEX__ += 1
        else:
            self.name = name

    # Getters
    def get_mass_distribution_name(self):
        return self.name

    def get_name(self): # Another way to get the name of the mass distribution
        return self.name

    def get_mass_distribution(self):
        return deepcopy(self.mass_distribution)

    def get_true_prop(self):
        return self.true_prop

    def get_proposition(prop_mass_pair):
        return prop_mass_pair[0]

    # Get the current sum of mass for this mass distribution
    def get_mass(self):
        mass = 0.
        for pmp in self.mass_distribution:
            mass = mass + pmp[1]

        if mass != 1.0:
            print("WARNING - MassDistribution: mass not equal to 1.0: ", mass)
        return min(mass, 1.0)


    # Setters
    def set_mass_distribution_name(self, name):
        self.name = name

    def set_name(self, name):   # Another way to set the name of the mass distribution.
        self.name = name

    def set_mass_distribution(self, mass_distribution):
        self.mass_distribution = deepcopy(mass_distribution)

    def set_true_prop(self, true_prop):
        self.true_prop = deepcopy(true_prop)


    # Adders
    def add_prop_mass_pair(self, prop_mass_pair):
        self.mass_distribution.append(prop_mass_pair)
        return deepcopy(self.mass_distribution)


    def replace_prop_mass_pair_mass(self, prop_mass_pair):
        found_prop = False  # set flag to indicate if proposition was found
        new_mass_distribution = []

        for pmp in self.mass_distribution:
            if pmp[0] == self.get_proposition(pmp):
                found_prop = True
                new_mass_distribution.add(deepcopy(prop_mass_pair))
            else:
                new_mass_distribution.add(deepcopy(pmp))

        if found_prop:
            self.mass_distribution = deepcopy(new_mass_distribution)
            return True
        return False

    def __str__(self):
        massdist_str = str(self.name)+": "+str(self.get_mass_distribution())
        return massdist_str


# Print imported message
if __name__ != "__main__":
    print ("The mass_distribution.py module has been successfully imported.")
else:
    print ("The mass_distribution.py is not intended to be executed, only imported.")

#//////////////////// END OF mass_distribution.py FILE ///////////////////////