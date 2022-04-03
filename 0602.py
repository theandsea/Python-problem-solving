def file_str2arr(fname):
    """
    convert file.txt to str[][]; remove punctuation,
    :param fname:
    :return:
    """
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    res = []
    with open(fname) as file:
        ctt = file.readline().lower()
        while len(ctt) > 0:
            for p in punc:
                ctt = ctt.replace(p, '')
            ctt = ctt.split(' ')
            line = []
            res.append(line)
            for word in ctt:
                if len(word) > 0:
                    line.append(word)

            ctt = file.readline().lower()

    return res


def encrypt_message(message, fname):
    '''
    Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    name of a text file source for the codebook, generate a sequence of 2-tuples that
    represents the `(line number, word number)` of each word in the message. The output is a list
    of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple.
    [(1394, 2), (1773, 11), (894, 10), (840, 1), (541, 2)]
    :param message: message to encrypt
    :type message: str
    :param fname: filename for source text
    :type fname: str
    :returns: list of 2-tuples
    '''
    assert isinstance(message, str) and isinstance(fname, str)
    assert message.islower()

    # get the tuple code for each word
    wdr = file_str2arr(fname)
    dic = {}
    for i in range(len(wdr)):
        for j in range(len(wdr[i])):
            word = wdr[i][j]
            if word in dic.keys():
                dic[word].append((i + 1, j + 1))
            else:
                dic[word] = [(i + 1, j + 1)]

    # encrypt each word; not randomized, just move forward to make sure not repeated
    stnc=message.split(' ')
    res=[]
    index={}
    for i in range(len(stnc)):
        word=stnc[i]
        assert word in dic.keys()
        if word not in index.keys():
            index[word]=0
        res.append(dic[word][index[word]])
        index[word] += 1

    return res


def decrypt_message(inlist, fname):
    '''
    Given `inlist`, which is a list of 2-tuples`fname` which is the
    name of a text file source for the codebook, return the encrypted message.
    :param message: inlist to decrypt
    :type message: list
    :param fname: filename for source text
    :type fname: str
    :returns: string decrypted message
    '''
    assert isinstance(inlist, list) and isinstance(fname, str)
    # check same
    for i in range(len(inlist)):
        tup = inlist[i]
        assert len(tup) == 2 and tup[0] >= 1 and tup[0] >= 1
        for j in range(i + 1, len(inlist)):
            assert tup != inlist[j]

    dic = file_str2arr(fname)

    stnc = []
    for i in range(len(inlist)):
        tup = inlist[i]
        stnc.append(dic[tup[0] - 1][tup[1] - 1])  # fix 1-based => 0-based

    return " ".join(stnc)

"""
code = [(1394, 2), (1773, 11), (894, 10), (840, 1), (541, 2), (1192, 5), (1984, 7), (2112, 6), (1557, 2), (959, 8),(53, 10), (2232, 8), (552, 5)]
print(decrypt_message(code, 'pg5200.txt'))

mess='let us not say we met late at the night about the secret'
print(encrypt_message(mess, 'pg5200.txt'))
"""
