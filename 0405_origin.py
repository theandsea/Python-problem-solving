orda = ord('a')
ordz = ord('z')
letter = []
for i in range(orda, ordz + 1):
    letter.append(chr(i))
print(letter)

def getletternum(w):
    letternum={}
    oldlen=len(w)
    for i in range(len(letter)):
        newlen=len(w.replace(letter[i],""))
        letternum[letter[i]]=oldlen-newlen
    return letternum

def cmpletternum(x,std):
    for key in std.keys():
        if x[key]>std[key]:
            return False
    return True

def letternum_sub(a,b): # a=a-b
    for key in a.keys():
        a[key] -=b[key]

def letternum_add(a,b): # a=a+b, works
    for key in a.keys():
        a[key] +=b[key]

def trydescrambler(strict,th,k,wds_len,solution): # involves restore, make it very complicated, you'd better use nested, not stack
    """
    return wdsolution
    :param strict:
    :param th:
    :param k:
    :param wds_len:
    :return:
    """
    sollist=[]
    wordlist=wds_len[k[th]]

    for word in wordlist:
        letternum=getletternum(word)
        if cmpletternum(letternum,strict):
            if th+1==len(k):
                sollist +=[solution+[word]] # cannot return, otherwise ignore other solution
            else:
                letternum_sub(strict, letternum)
                solution.append(word)
                sollist += trydescrambler(strict, th+1, k, wds_len, solution)
                solution.pop()
                letternum_add(strict, letternum)
    return sollist


def descrambler(w,k):
    """
    given a sequence of n lower-case letters and a k-tuple of integers that indicate partition-lengths of the sequence.
    iteratively yield the output
    :param w:
    :param k:
    :return:
    """
    assert isinstance(w,str) and isinstance(k,tuple)
    for char in w:
        assert orda<=ord(char) and ord(char)<=ordz # lower-case
    for num in k:
        assert num>0 # length > 0

    strict_dic=getletternum(w)
    print(strict_dic)

    # process the valid words, excluding words exceeding the strict
    with open("xxx.txt") as file:
        totalstr=file.read()
        words=totalstr.split("\n")
    wds_len=[[] for i in range(19)]
    for word in words:
        if cmpletternum(getletternum(word),strict_dic):
            wds_len[len(word)].append(word)

    # deep process the valid words, organize the level-order dictionary


    # using a DFS to get all the solution and generate iteratively
    solution=[]
    solist=trydescrambler(strict_dic, 0, k, wds_len, solution)
    yield from solist


    """wdsolution=["" for i in range(len(k))]
    index=[0 for i in range(len(k))]
    th=0
    endlen=len(k)
    while th>=0:
        # search for th-th word
        wordlist=wds_len[k[th]]
        if index[th]<len(wordlist):
            # before find another, restore the letternum
            if index[th]!=0: # wipe old
                letternum_add(strict_dic, getletternum(wdsolution[th],letter))
            find=False
            for i in range(index[th], len(wordlist)):  # begin from record
                letternum = getletternum(wordlist[i], letter)
                if cmpletternum(letternum, strict_dic):  # valid
                    wdsolution[th] = wordlist[i] + ""
                    index[th] = i + 1  # next search
                    if th + 1 == endlen:  # if complete yield
                        yield wdsolution
                    else:  # deeper
                        letternum_sub(strict_dic,letternum) # substract alrady used letter
                        th += 1
                        index[th] = 0
                        find=True
                        break
            if not find: # nothing
                index[th]=len(wordlist)
        else: # this level exhausted, upper
            th -=1"""


w = 'trleeohelh'
k=(5,5)
x=descrambler(w,k)
""""""
# x=descrambler('choeounokeoitg',(3,5,6))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

