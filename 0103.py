
def compute_average_word_length(instring,unique=False):
    """
    compute the average length of the words in the input string (instring)
    :param instring:
    :param unique: If the unique option is True, then exclude duplicated words.
    :return:
    """
    s=instring
    assert isinstance(s,str)
    # other $ /n special symbol ??

    # convert to lowercase
    s=s.lower()
    sen=s.split(" ")

    # unique=True
    if not unique: # false, compute directly
        t=0
        ls=0
        for word in sen:
            t+=1
            ls+=len(word)
        return ls/t
    else: # compute without repetition
        t=0
        ls=0
        dic={}
        for word in sen:
            if word not in dic.keys():
                t+=1
                ls+=len(word)
                dic[word]=True
        return ls/t

"""
print(compute_average_word_length("Mary had a little"))
print(compute_average_word_length("Mary had a little lamb its fleece was white as snow and everywhere that Mary went the lamb was sure to go"))
"""



