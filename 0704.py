import random

import numpy as np
import pandas as pd

def add_month_yr(x):
    """
     x is a pd.DataFrame and returns the same pd.DataFrame with the new column
    :param x:
    :return:
    """
    assert isinstance(x,pd.DataFrame)
    mthyr=[]
    time=x["Timestamp"]

    for i in range(len(time)):
        stamp=pd.to_datetime(time[i])
        day=stamp.month_name()[:3]+"-"+str(stamp.year)
        mthyr.append(day)

    x['month-yr']=mthyr
    return x


def fix_categorical(x):
    """
    x is a pd.DataFrame with the required "month-yr" column and output is a pd.DataFrame with the "month-yr" column having the categorical dtype
    :param x:
    :return:
    """
    assert isinstance(x,pd.DataFrame)
    x=add_month_yr(x)
    # print(pd.Categorical(x['month-yr']))
    # x=fix_categorical(add_month_yr(x))
    cate=list(x['month-yr'].astype('category').cat.categories)
    time=[]
    for i in range(len(cate)):
        time.append(pd.to_datetime(cate[i]))
    cate=sorted(cate,key=lambda i:time[cate.index(i)])
    cate = pd.CategoricalDtype(cate,ordered=True) # set ordered = True; otherwise considered wrong
    # look official document(type in CategoricalDatype), most reliable
    x['month-yr'] = x['month-yr'].astype(cate)
    # x=pd.Series(x['month-yr'],dtype=cate)
    # print(x['month-yr'])
    # print(x.groupby('month-yr')['Timestamp'].count().to_frame().sort_index())
    return x

"""
dtypes = {'some_categorical_column': 'category'}
x = pd.read_csv('survey_data.csv', dtype=dtypes)
x= fix_categorical(add_month_yr(x))
print(x.groupby('month-yr')['Timestamp'].count().to_frame().sort_index())
"""

