def slide_window(x,width,increment):
    """
    Implement a sliding window for an arbitrary input list
    :param x:
    :param width:
    :param increment:
    :return:
    """
    assert isinstance(x,list) and isinstance(width,int) and isinstance(increment,int)
    assert width>0 and increment>0 and len(x)>=width

    res=[]
    end=width
    while end<=len(x):
        res.append(x[end-width:end])
        end += increment

    return res

# print(slide_window(list(range(18)),5,2))
