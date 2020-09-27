#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:14:24 2020

Giving the height of release, the bouncing coefficient of the object
and a height of a window where the window is between the height of 
drop and the ground.

Returns the number of times someone in the window would see the ball 

or  -1 if an error in input occured. 

@author: TjH
"""


def bouncing_ball(h, bounce, window):
    if h <= 0:
        return -1
    elif  1 < bounce <= 0 or bounce > 0.9999999 or bounce == 1:      
        return -1
    elif window > h:
        return -1
    seen = 0
    while h > window: 
        h = h * bounce
        seen +=2
    return seen -1
