def map_bitstring(x):
    """
    takes a list of bitstrings (i.e., 0101) and
    maps each bitstring to 0 if the number of 0s in the bitstring strictly exceeds the number of 1s.
    Otherwise, map that bitstring to 1
    :param x:
    :return:
    """
    assert isinstance(x,list)
    for bitstr in x:
        assert bitstr.replace("0","").replace("1","")=="" # strictly bitstring

    res={}
    for bitstr in x:
        if bitstr not in res.keys():
            if len(bitstr.replace("1",""))>len(bitstr.replace("0","")): # only 0 left > only 1 left
                res[bitstr]=0
            else:
                res[bitstr]=1

    return res


def gather_values(x):
    """
    tally the number of times an existing key is repeated
    Generate a new dictionary with bitstrings as keys and with values as lists that contain the corresponding mapped values from map_bitstring
    :param x:
    :return:
    """
    assert isinstance(x,list)
    mapnum=map_bitstring(x) # already check the format a lot

    res={}
    for i in range(len(x)):
        bitstr=x[i]
        value=mapnum[bitstr]
        if bitstr in res.keys():
            res[bitstr].append(value)
        else:
            res[bitstr]=[value]

    return res

""""""
# x=['10', '11', '01', '00', '10', '00', '00', '11', '10', '00', '00', '01', '01', '11', '10', '00', '11', '10', '11', '11']
x=['1111', '0110', '1001', '0011', '0111', '0100', '0111', '1100', '0011', '0010', '0010', '1010', '1010', '1100', '0110', '0101', '0110', '1111', '1001', '0110', '0010', '1101', '0101', '0010', '0100', '0010', '0000', '0000', '0011', '0110', '0101', '1010', '1011', '1101', '1100', '0111', '1110', '0100', '0110', '1101', '0001', '1110', '0010', '0001', '1010', '1010', '0011', '1000', '0010', '0000', '1010', '1101', '1111', '1000', '1000', '0010', '1010', '0101', '0101', '1101', '0110', '1001', '1100', '1100', '1000', '1010', '0011', '0101', '0101', '0011', '0001', '1010', '0011', '0011', '1101', '1010', '0101', '0011', '1011', '0101', '0000', '1111', '1001', '0101', '1100', '0011', '1111', '1101', '0001', '1111', '1110', '1111', '0001', '0010', '0110', '0100', '0101', '1100', '1110', '1001']
res=gather_values(x)
for key in res.keys():
    print(key,res[key])




