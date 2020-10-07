#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:10:37 2020

Given an array of "Stock prices", return the max profit given you are only
allowed to by and sell once.

@author: Tj,
"""
import math


def max_profits(arr):
    profit = -math.inf
    lowest_value_seen = math.inf
    # Iterate through every element in the array
    for current in range(1,len(arr)):
        # Find the lowest point in the array 
        if arr[current] < lowest_value_seen:
            lowest_value_seen = arr[current]
        # If the current lowest stock yeilds a beter profit than seen update
        # profit
        if arr[current] - lowest_value_seen > profit:
            profit = arr[current] - lowest_value_seen
    # return max profit
    return profit
    
    

