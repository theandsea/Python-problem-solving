import os

def split_by_n(fname,n=3):
    '''
    Split files into sub files of near same size
    fname : Input file name
    n is the number of segments
    '''
    assert isinstance(n,int) and n>=1
    assert isinstance(fname,str)

    size=os.path.getsize(fname) # each char take 1 bytes
    step=size//n
    nowl=0
    nextlen=0
    newfile=None
    i = 0
    with open(fname) as file:
        while True:
            # read
            ctt = file.readline()
            if len(ctt)==0: # empty string for end
                newfile.close()
                break

            # whether start a new one
            if nowl >= nextlen:
                num = str(i)
                num = "000"[:3 - len(num)] + num
                if newfile is not None:
                    newfile.close()
                newfile = open(fname + "_" + num + ".txt", 'w')
                nextlen += step
                i += 1

            # write
            newfile.write(ctt)
            nowl += len(ctt)


# split_by_n('pg5200.txt',n=8)
