# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:24:37 2024

@author: Lab
"""
import math
def average(a, b):
    """Given parameters a and b, compute and
       return the arithmetic mean of a and b"""
    return (a + b) * 0.5


def distance(a, b):
    """Given points a and b, compute and
       absolute value of the difference of a and b to find distance between them"""
    return abs(a-b)

def geometric_mean(a, b):
    """Given sides a and b, compute and
       square root of the product of a and b to find the geometric mean"""
    return math.sqrt(a*b)
      
def pyramid_volume(A, h):
    """Given base area A and height h of a pyramid, compute and return the product 
        of A and h divided by 3 to find the volume of the pyramid"""
    return (A*h)/3

    