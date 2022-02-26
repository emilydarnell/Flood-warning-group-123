from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def polyfit(dates, levels, p):
    converted_dates = matplotlib.dates.date2num(dates)
    shift = np.min(converted_dates)
    shifted_dates = converted_dates - shift
    poly = poly = np.poly1d(np.polyfit(shifted_dates, levels, p))
    
    return poly, shift

