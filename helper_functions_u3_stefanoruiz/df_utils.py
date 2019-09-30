"""
Helper function for dataframes, numpy arrays, and splitting city, state, and country
with REGEX
"""

import pandas
import numpy

def check_null(data):
    ## Checks if pandas dataframe contains null values.
    name =[x for x in globals() if globals()[x] is data][0]
    null_values = pandas.isnull(data).sum()
    
    if null_values.any():
        print("%s contains NaN values" % name)
        print('*****************\n', null_values, '\n*****************')
    else:
        print("%s contains no NaN values." % name)

def city_statesplit(data):
    # Will create new features if the features are not found.
    data[["city", "state", "zip"]] = data.address.str.extract(
        '^([^,]+),\s([A-Z]{2})(?:\s(\d{5}))?$',expand=True)

