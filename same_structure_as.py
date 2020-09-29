#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 08:36:27 2020
same_structure_as(list, list):
    
    given two lists, returns True if their structures are identical otherwise returns False
    Suitable for small, uncomplicated comparisons. O(n^2) worst case, O(1) best case

@author: TjH
"""

def same_length(original, other):
    try:
        return len(original) == len(other)
    except TypeError:
        if isinstance(original, [int, float]) and isinstance(other, [int, float]):
            return True
        else:
            return False
        
        
def same_structure_recur(ele1, ele2):
    if not same_length(ele1,ele2):
        return False
    else:
        for i in range(len(ele1)):
            if isinstance(ele1[i], list) and isinstance (ele2[i], list):
                return same_structure_recur(ele1[i], ele2[i])
        

def same_structure_as(original, other):
    # check if the lists are of the same length:
    if same_length(original, other):
        # compare each element of the array, recursively
        for i in range(len(original)):
            if not same_structure_recur(original[i], other[i]):
                return False
        return True
    else:
        return False
        
