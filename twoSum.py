#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 09:22:58 2020

A function that takes as input a list of integers a target integer.

It returns the indices of the two numbers that add together to make the target



@author: TjH
"""
class Solution:
    def twoSum(self, nums, target):
        h = {} # create an empty dictionary
        for i, num in enumerate(nums):
            # the complimentary number MUST be the target delta and itself
            n = target - num
            # If the complimentary number is not in the list, set num to 1
            if n not in h:
                h[num] = i
            else:
                # if complimentary number is in the list return the current 
                # indices and the indice where n exists!!! awesome
                return [h[n], i]

