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