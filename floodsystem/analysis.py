"""This module contains a collection of functions related to performing analysis of the
water station data
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def polyfit(dates, levels, p): #Plots a polynomial of set order, that most closely mtaches an accurate plot of the water levels
   
    #from a list of datetime objects returns a list of float, where the floats are the time in days (including fractions of days) since the year 0001
    x = matplotlib.dates.date2num(dates)

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(x-x[0], levels, p)

    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)

    #The function should return a tuple of (i) the polynomial object and (ii) any shift of the time (date) axis
    return (poly, dates[0])
