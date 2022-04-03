def write_chunks_of_five(words,fname):
    """
    a new file that consists of each consecutive non-overlapping sequence of five lines merged into one line
    :param words:
    :param fname:
    :return:
    """
    assert isinstance(words,list) and isinstance(fname,str)
    for word in words:
        assert isinstance(word,str)

    with open(fname, "w") as f:
        n=len(words)
        line=n//5
        # full line
        index=0
        for i in range(line):
            sentence=""
            for j in range(5):
                sentence += " "+words[index]
                index+=1
            sentence=sentence[1:]+"\n"
            f.write(sentence)
        # rest line
        if index<n:
            sentence = ""
            while index<n:
                sentence += " "+words[index]
                index+=1
            sentence=sentence[1:]+"\n"
            f.write(sentence)

"""
wordlist=["the","of","and","of","a","in","for","is","on","that","by"]
write_chunks_of_five(wordlist,"xxx.txt")
"""

