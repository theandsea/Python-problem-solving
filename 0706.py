class Rational:
    def __init__(self,a,b):
        assert isinstance(a,int) and isinstance(b,int) and b != 0
        if a==0:
            self.a=0
            self.b=1
        else:
            l=self.GCF(abs(a),abs(b))
            self.a=abs(a)//l
            self.b=abs(b)//l
            if a*b<0:
                self.a=-self.a

    def GCF(self,a,b):
        # GCF
        l=min(a,b)
        h=max(a,b)
        while h % l !=0:
            h %= l
            h,l=l,h
        return l

    def __repr__(self):
        if self.b == 1:
            return str(self.a)
        elif self.a==0:
            return "0"
        else:
            strnum=str(self.a)+"/"+str(self.b)
            return strnum

    def __rtruediv__(self, other): # divide others
        if isinstance(other,Rational):
            return Rational(self.a*other.b,self.b*other.a)
        elif isinstance(other,int):
            return Rational(self.b*other,self.a)

    def __int__(self):
        return self.a//self.b

    def __float__(self):
        return self.a/self.b

    def __mul__(self, other):
        if isinstance(other,Rational):
            a = self.a*other.a
            b = self.b*other.b
            return Rational(a, b)
        elif isinstance(other,int):
            a = self.a * other
            b = self.b
            return Rational(a, b)

    def __truediv__(self,other): # for /, divided by other
        if isinstance(other, Rational):
            a = self.a * other.b
            b = self.b * other.a
            return Rational(a, b)
        elif isinstance(other, int):
            a = self.a
            b = self.b * other
            return Rational(a, b)

    def __sub__(self, other):
        assert isinstance(other,Rational)
        a=self.a*other.b-other.a*self.b
        b=self.b*other.b
        return Rational(a,b)

    def __add__(self, other):
        assert isinstance(other,Rational)
        a = self.a * other.b + other.a * self.b
        b = self.b * other.b
        return Rational(a, b)

    def __neg__(self):
        return Rational(-self.a,self.b)

    def __eq__(self, other):
        diff=self.diff(other)
        if diff == 0:
            return True
        else:
            return False

    def diff(self, other):
        diff = self.a * other.b - other.a * self.b
        return diff

    def __lt__(self, other): # capital
        if self.diff(other)<0:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.diff(other)>=0:
            return True
        else:
            return False

    def __abs__(self):
        return Rational(abs(self.a),abs(self.b))


def square_root_rational(x,abs_tol=Rational(1,1000)):
    """
    returns the square root of x to absolute precision abs_tol.
    :param x:
    :param abs_tol:
    :return:
    """
    assert isinstance(x,Rational) and x >= Rational(0,1)

    l=Rational(0,1)
    r=Rational(10000000000,1)

    while abs_tol<(abs(r-l)*10):
        mid = (r+l)/2
        if x <= mid*mid:
            r=mid
        else:
            l=mid

    return mid

"""
x=square_root_rational(Rational(5,1))
print(x)
print(float(x))

import math
print(abs(math.sqrt(5)-float(x)))
"""

