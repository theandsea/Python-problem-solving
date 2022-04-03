import copy
from typing import Dict


class Polynomial:
    def __init__(self,dic): # init != ini !
        """
        Create a Python class that can implement a univariate polynomial (Polynomial) over the field of integers
        :param dic:
        :return:
        """
        assert isinstance(dic, dict)
        for key in dic:
            assert isinstance(key, int) and isinstance(dic[key], int)

        self.dic = {}
        # eliminate the 0
        for key in dic.keys():
            if dic[key] != 0:
                self.dic[key] = dic[key]

    def __repr__(self):
        if len(self.dic) ==0:
            return '0'

        dic = self.dic
        keylist = list(dic.keys())
        keylist.sort()
        term = []
        for i in range(len(keylist)):
            t=keylist[i]
            coe=dic[keylist[i]]
            if t==0:
                termstr=str(coe)
            elif t==1:
                if coe==1:
                    termstr="x"
                elif coe==-1:
                    termstr="-x"
                else:
                    termstr=str(coe)+" x"
            else:
                # coefficient
                if coe == 1:
                    termstr = "x^(" + str(t) + ")"
                elif coe == -1:
                    termstr = "-x^(" + str(t) + ")"
                else:
                    termstr = str(coe) + " x^(" + str(t) + ")"
            term.append(termstr)

            """# coefficient:
            if abs(dic[keylist[i]]) != 1 or keylist[i] == 0:  # 1/-1 omitted; constant must have
                termstr = str(dic[keylist[i]])
            else:
                termstr = ""
            print(termstr)
            # term
            if keylist[i] == 1:
                termstr += "x"
            elif keylist[i] == -1:
                termstr += "-x"
            elif keylist[i] !=0:
                termstr += " x^(" + str(keylist[i]) + ")"
            term.append(termstr)
            print(termstr)"""

        # join but for '-'
        if dic[keylist[0]]>0: # first term ??
            res = term[0]
        else: # <0, 0 has been excluded
            res = '- '+term[0][1:]
        for i in range(1,len(keylist)):
            if dic[keylist[i]]>0:
                res += " + "+term[i]
            else:
                res += " - "+term[i][1:]
        return res

    def __mul__(self, other):
        if isinstance(other,int):
            dic={}
            for key in self.dic:
                dic[key]=self.dic[key] * other
            return Polynomial(dic)
        elif isinstance(other,Polynomial):
            dic={}
            dic_a=self.dic
            dic_b=other.dic
            for a in dic_a:
                for b in dic_b:
                    key=a+b
                    c=dic_a[a]*dic_b[b]
                    if key in dic:
                        dic[key] += c
                    else:
                        dic[key] =c
            return Polynomial(dic)
        else:
            assert False

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        if isinstance(other,int):
            dic = copy.copy(self.dic)
            if 0 in dic:
                dic[0] += other
            else:
                dic[0] = other
            return Polynomial(dic)
        elif isinstance(other,Polynomial):
            dic = copy.copy(self.dic)
            for key in other.dic:
                if key in dic:
                    dic[key] += other.dic[key]
                else:
                    dic[key] = other.dic[key]
            return Polynomial(dic)
        else:
            assert False

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        return self.__mul__(-1)

    def __sub__(self, other):
        return self.__add__(-other)

    def subs(self,val):
        """
        substitute in integers and evaluate
        :param value:
        :return:
        """
        s = 0
        for key in self.dic:
            s += self.dic[key] * pow(val,key)
        return s

    def __eq__(self, other):
        if isinstance(other,int):
            if len(self.dic)==0 and other==0:
                return True
            elif len(self.dic)==1 and other != 0 :
                return self-other == 0
            else:
                return False
        elif isinstance(other,Polynomial):
            return self-other == 0
        else:
            assert False

    def __truediv__(self, other): # for /
        if isinstance(other,int):
            assert other != 0
            dic={}
            for key in self.dic:
                if self.dic[key] % other == 0:
                    dic[key] = self.dic[key] // other
                else:
                    raise NotImplemented
            return Polynomial(dic)
        elif isinstance(other,Polynomial):
            dic=copy.copy(self.dic)
            key_max=max(dic.keys())
            ddl=min(dic.keys())
            key_om=max(other.dic.keys())
            res={}
            dic_o=other.dic
            while len(dic)>0 and max(dic.keys()) >= ddl:
                keyi=max(dic.keys())
                if dic[keyi] != 0:
                    if dic[keyi] % dic_o[key_om] == 0:
                        ratio=dic[keyi] // dic_o[key_om]
                        dat=keyi-key_om
                        res[dat]=ratio
                        for k in dic_o:
                            if k+dat in dic:
                                dic[k+dat] -= dic_o[k] * ratio
                            else:
                                dic[k+dat] = -dic_o[k] * ratio
                    else:
                        raise NotImplemented
                else:
                    dic.pop(keyi)
            if len(dic)==0:
                return Polynomial(res)
            else:
                raise NotImplemented
        else:
            assert False

"""
p = Polynomial({0:8,1:2,3:4})
q=Polynomial({0:8,1:2,2:8,4:4})
print(repr(p))
print(p * 3)
print(3*p)
print(p+q)
print(p*4 + 5 - 3*p - 1)
print(type(p-p))
print(p*q)
print(p.subs(10))
print((p-p+10) == 10)
print(p==q)

p=Polynomial({0:8,1:0,3:4})
print(repr(p))



p = Polynomial({5:1,0:-1})
q = Polynomial({1:1,0:-1})
print(p/q)
print(-p/q)
"""





