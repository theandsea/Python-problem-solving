def write_columns(data,fname):
    """
    Write a function that can write the following formula to three columns to a comma-separated file:
    data_value, data_value**2, (data_value+data_value**2)/3.
    :param data:
    :param fname:
    :return:
    """
    assert isinstance(fname,str) and isinstance(data,list)
    # check each element in data
    for num in data:
        assert isinstance(num,int) or isinstance(num,float)

    # compute
    with open(fname,"w") as f:
        for num in data:
            res = "{0},{1},{2.real:.2f}\n".format(num, num ** 2, (num + num ** 2) / 3)
            f.write(res)

"""
thisdata=[500,4,6,1,9,0,3,9,2,7,10,8,4,7,1,2,7,6,5,2,8,2,0,1,1,1,2,10,6,2]
write_columns(thisdata,"xxx.txt")
"""

