import numpy as np
import pandas as pd


def split_count(x):
    """
    x is a pd.Series object and it returns a pd.DataFrame object.
    :param x:
    :return:
    """
    assert isinstance(x, pd.Series)
    cls = []
    for strcls in x:
        for word in strcls.split(', '):
            cls.append(word)
    s = pd.Series(range(len(cls)),index=cls) # index and data !!
    # print(s)
    count = s.groupby(by=lambda i: i)
    frame = pd.DataFrame(count.count())
    """print(type(count.count()))
    print(count.count())"""
    # print(frame)
    return frame

"""
dtypes = {'some_categorical_column': 'category'}
x = pd.read_csv('survey_data.csv', dtype=dtypes)["Is there anything in particular you want to use Python for?"]
print(type(x))
# print(x)
split_count(x)
"""
"""
dates = pd.date_range('20130101', periods=12)
s = pd.Series(range(12), index=dates)
print(s)
print(s.groupby(by=lambda i: i.a).count())
"""

