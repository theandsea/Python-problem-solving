import random

def multinomial_sample(n, p, k=1):
    '''
    Return samples from a multinomial distribution(times for each side). multinomial_sample(10,[1/3,1/3,1/3],k=10)
    similar to binomial
    n:= number of trials in each sample
    p:= list of probabilities
    k:= number of desired samples
    '''
    assert isinstance(n,int) and n>=1 and isinstance(k,int) and k>=1
    assert isinstance(p,list)

    prsum=[]
    s=0
    lp=len(p)
    for i in range(lp):
        s += p[i]
        prsum.append(s)
    assert abs(s - 1.) < 0.00001

    sample=[]
    for i in range(k):
        line=[0 for i in range(lp)]
        sample.append(line)
        for j in range(n):
            rdm=random.random()
            for z in range(lp):
                if rdm <= prsum[z]:
                    line[z] += 1
                    break

    return sample



# print(multinomial_sample(10,[1/3,1/3,1/6,1/6]))
