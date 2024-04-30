# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 02:13:53 2024

@author: Lab
"""

import math
def degree(x):
    """Given a radian x, compute the product of x 360 divided by two pie to 
       find the value in degree"""
    return x * (360 / (2 * math.pi))

def min_max(xs):
    """Given a list xs, find the minimum value xmin and the maximum value xmax
    in the list, and return a tuple (xmin, xmax)"""
    xmax = []
    xmin = []
    for i in [xs]:
        if xs[i] == math.max:
            xmax = xs[i]
        if xs[i] == math.min:
            xmin = xs[i]
    return (xmin, xmax)