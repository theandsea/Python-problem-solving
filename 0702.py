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
    """
    z=pd.to_datetime(time[0])
    print(z)
    print(z.month_name()[:3])
    print(z.year)
    """
    for i in range(len(time)):
        stamp=pd.to_datetime(time[i])
        day=stamp.month_name()[:3]+"-"+str(stamp.year)
        mthyr.append(day)
    # print(mthyr)

    x['month-yr']=mthyr
    return x


"""
dtypes = {'some_categorical_column': 'category'}
x = pd.read_csv('survey_data.csv', dtype=dtypes)
print(add_month_yr(x))
"""


