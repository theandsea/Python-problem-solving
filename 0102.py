def convert_hex_to_RGB_single(s):
    """
    convert hex-codes (e.g., ['#FFAABB']) into RGB-tuples [(255,170,187)]
    :return:
    """
    assert isinstance(s,str) and len(s)==7 and s[0]=='#' # format error

    # check format within 0-9 or A-F
    ord0=ord('0')
    ord9=ord('9')
    ordA=ord('A')
    ordF=ord('F')
    for i in range(1,7):
        num=ord(s[i])
        if (ord9<num or num<ord0) and (ordF<num or num<ordA):
            assert False # digit should be within 0-9, A-F

    # convert
    r = int(s[1:3], 16)
    g = int(s[3:5], 16)
    b = int(s[5:], 16)

    return (r,g,b)


def convert_hex_to_RGB(s):
    """
    convert a list of hex-codes (e.g., ['#FFAABB']) into a list of RGB-tuples [(255,170,187)]
    :param s:
    :return:
    """
    assert isinstance(s,list) # must be a list

    # convert each of them
    res=[]
    for i in range(len(s)):
        res.append(convert_hex_to_RGB_single(s[i]))

    return res



"""
print(convert_hex_to_RGB(['#FFAABB']))
print(convert_hex_to_RGB(["#FFAAABB"]))
print(convert_hex_to_RGB(["#FFxABB"]))
"""


