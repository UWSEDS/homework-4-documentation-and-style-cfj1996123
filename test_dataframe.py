""" test_dataframe is a module to check whether the data frame satisfies some conditions or not.

It provides the following functions to check the data frame.

- sanity_check
- type_check
- nan_check
- row_check

Also, there are functions to test the above four functions, they are:

- test_sanity_check
- test_type_check
- test_nan_check
- test_row_check

"""

import pandas as pd
import numpy as np

def sanity_check(test_dataframe, colnames):
    """
    :param test_dataframe:        pandas data frame
    :param colnames:  list[str]
    :return:          bool, whether all conditions are met.
    """
    # test whether all columns are specified in colnames
    colnames_set = set(colnames)
    for col in test_dataframe.columns:
        if col not in colnames_set:
            return False
    # test whether all elements in the same column have the same type
    for col in test_dataframe.columns:
        for i in range(len(test_dataframe[col])):
            elem = test_dataframe[col][i]
            if type(elem) != type(test_dataframe[col][0]):
                return False

    # test whether there is at least 10 rows
    if test_dataframe.shape[0] < 10:
        return False

    return True

def type_check(test_dataframe):
    """
    :param test_dataframe: pandas data frame
    :return:   bool, whether all values in same column have same type.
    """
    for col in test_dataframe.columns:
        for i in range(len(test_dataframe[col])):
            elem = test_dataframe[col][i]
            if type(elem) != type(test_dataframe[col][0]):
                return False
    return True

def nan_check(test_dataframe):
    """
    :param test_dataframe: pandas data frame
    :return:   bool, whether there is any missing value in the data frame.
    """
    return test_dataframe.isnull().values.any()

def row_check(test_dataframe):
    """
    :param test_dataframe: pandas data frame
    :return: bool, whether there is no less than 1 row in the data frame.
    """
    return test_dataframe.shape[0] >= 1

def test_sanity_check():
    """
    test function sanity_check
    """
    testset = {'col1': list(range(20)), 'col2': [chr(i) for i in range(20)]}
    test_dataframe = pd.DataFrame(data=testset)
    assert sanity_check(test_dataframe, ['col1', 'col2']) is True

def test_type_check():
    """
    test function type_check
    """
    testset = {'col1': list(range(19))+['a'], 'col2': [chr(i) for i in range(20)]}
    test_dataframe = pd.DataFrame(data=testset)
    assert type_check(test_dataframe) is False

def test_nan_check():
    """
    test function nan_check
    """
    testset = {'col1': list(range(19))+[np.nan], 'col2': [chr(i) for i in range(20)]}
    test_dataframe = pd.DataFrame(data=testset)
    assert nan_check(test_dataframe) == True


def test_row_check():
    """
    test function row_check
    """
    test_dataframe = pd.DataFrame()
    assert row_check(test_dataframe) is False
