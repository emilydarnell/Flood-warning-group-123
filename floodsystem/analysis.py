from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def polyfit(dates, levels, p):
    """Returns a polynomial of degree p representing the best fit for a function
    f(dates) = levels. It offsets dates such that the minimum value of the domain
    is equal to 0 to prevent floating point errors. The offset is returned alongside
    the polynomial as (polynomial,offset)."""
    converted_dates = matplotlib.dates.date2num(dates)
    shift = np.min(converted_dates)
    converted_dates = converted_dates - shift
    poly = np.poly1d(np.polyfit(converted_dates, levels, p))

    return poly, shift