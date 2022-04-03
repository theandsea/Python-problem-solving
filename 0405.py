def getletternum(w):
    letternum={}
    oldlen=len(w)
    letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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
    orda = ord('a')
    ordz = ord('z')
    assert isinstance(w,str) and isinstance(k,tuple)
    for char in w:
        assert orda<=ord(char) and ord(char)<=ordz # lower-case
    for num in k:
        assert num>0 # length > 0

    strict_dic=getletternum(w)

    # process the valid words, excluding words exceeding the strict
    with open("/tmp/google-10000-english-no-swears.txt") as file:
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
    # like this 'one tough cookie'
    for sol in solist:
        res=""
        for i in range(len(sol)):
            res += sol[i]+" "
        res=res[:-1]
        yield res


"""
w = 'trleeohelh'
k=(5,5)
x=descrambler(w,k)

x=descrambler('choeounokeoitg',(3,5,6))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

x=list(descrambler('qeodwnsciseuesincereins',(4,7,12)))
print(list(x))
"""

