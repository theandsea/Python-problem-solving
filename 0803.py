def next_permutation(t:tuple)->tuple:
    """
    Given a permutation of any length, generate the next permutation in lexicographic order.
    :param t:
    :return:
    """
    assert isinstance(t,tuple)
    for num in t:
        assert isinstance(num,int) and num >=0

    nums = list(t)
    numssorted=sorted(nums,key=lambda x:x)
    for i in range(len(numssorted)-1):
        if numssorted[i] == numssorted[i+1]:
            assert False

    nowmax=nums[-1]
    st=[nowmax]
    targ=-1
    for i in reversed(range(len(nums)-1)):
        if nums[i]<nowmax:
            targ=nums[i]
            st.append(targ)
            break
        else:
            nowmax=nums[i]
            st.append(nowmax)

    # print(st)
    # print(i,targ)
    st.sort()
    if targ != -1:
        nextfirst=st.pop(st.index(targ)+1)
        newsort=nums[:i]+[nextfirst]+st
        return tuple(newsort)
    else:
        return tuple(st)


# print(next_permutation(111))
"""
print(next_permutation((2,3,1)))
print(next_permutation((0, 5, 2, 1, 4, 7, 3, 6)))
print(next_permutation((2, 3, 1)))
"""
