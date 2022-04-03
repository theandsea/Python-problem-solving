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


def count_month_yr(x):
    """
    x is a pd.DataFrame that returns a pd.DataFrame
    :param x:
    :return:
    """
    assert isinstance(x,pd.DataFrame)
    x=add_month_yr(x)
    # x = x.groupby('month-yr')['Timestamp'].count().to_frame()) # this can also do all the job !!!
    """"""
    s = pd.Series(range(len(x)), index=x['month-yr'])
    count = s.groupby(by=lambda i: i).count()
    frame = pd.DataFrame({"Timestamp":count}) # index remained

    # frame["Timestamp"]=count
    # print(frame)
    return frame


""""""
dtypes = {'some_categorical_column': 'category'}
x = pd.read_csv('survey_data.csv', dtype=dtypes)
print(count_month_yr(x))


