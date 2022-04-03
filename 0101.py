
def is_string_integer(s):
    """
    returns True or False if that character represents a valid integer in base 10
    """
    assert isinstance(s,str) and len(s)==1
    # a single string character (i.e., 'a','b','c')

    # first check if within 0-9
    ord0=ord('0')
    ord9=ord('9')
    for ch in s:
        if ord(ch)<ord0 or ord(ch)>ord9:
            return False

    # second check if 0 in the first place
    if len(s)==1: # 0-9
        return True
    elif s[0]=='0':
        return False
    else:
        return True

"""
print(is_string_integer("1"))
print(is_string_integer("1711"))
print(is_string_integer("0111"))
print(is_string_integer(""))
print(is_string_integer(111))
"""


