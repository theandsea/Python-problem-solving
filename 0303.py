import calendar
import datetime

def number_of_days(year,month):
    """
    returns the number of calendar days in a given year and month
    :param year:
    :param month:
    :return:
    """
    assert isinstance(year,int) and isinstance(month,int)
    assert year>0
    assert 1<=month and month<=12
    _,s=calendar.monthrange(year,month)
    return s


def number_of_leap_years(year1,year2):
    """
    find the number of leap-years between (including both endpoints) two given years.
    :param year1:
    :param year2:
    :return:
    """
    assert isinstance(year1,int) and isinstance(year2,int)
    assert year1<=year2 and year1>0 and year2>0
    s=0
    for i in range(year1,year2+1):
        if calendar.isleap(i):
            s +=1
    return s


def get_day_of_week(year,month,day):
    """
    find the string name (e.g., Monday, Tuesday) of the day of the week on a given month,day, and year.
    :param year:
    :param month:
    :param day:
    :return:
    """
    assert isinstance(year,int) and isinstance(month,int) and isinstance(day,int)
    assert year>0
    assert 1<=month and month<=12
    assert 1<=day and day<=number_of_days(year,month)

    # weekname = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # weeknum =datetime.date(year, month, day).weekday()
    weeknum=calendar.weekday(year,month,day)
    return calendar.day_name[weeknum]


"""
print(number_of_days(2022,1))
print(number_of_leap_years(2000,2008))
print(get_day_of_week(2022,1,31))
"""
