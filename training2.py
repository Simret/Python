# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:11:24 2024

@author: Lab
"""
import math
def box_volume(a, b, c):
    """Given edges of cuboid a, b and c, compute and
       return product of a, b and c to find the volume"""
    return (a * b * c)

def fall_time(h):
    """Given height of a tower h, compute and
       return the square root of the quotient of double height to gravity to find the time 
       needed for an object to fall to the ground"""
    return math.sqrt((2 * h) / 9.81)

def interval_point(a, b, x):
    """Given points a and b, compute the difference and multiply it by x and add a 
       to the result to find the position"""
    return a + (b - a) * x

def impact_velocity(h):
    """Given height h, compute the velocity v multiplying 9.81 fall_time(h)"""
    return (fall_time(h)) * 9.81

def signum(x):
    """Given a number x, return 1 if x is greater than 0, return 0 if x is 0 return -1 otherwise"""
    if (x > 0):
        return 1
    if (x == 0):
        return 0
    else:
        return -1