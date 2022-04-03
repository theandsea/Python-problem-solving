class Rational:
    def __init__(self,a,b):
        assert isinstance(a,int) and isinstance(b,int) and b != 0
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

    def __rtruediv__(self, other): # divided by !!!!
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

    def __truediv__(self,other): # for /
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

"""
r=Rational(3,4)
print(repr(r))
print(-1/r)
# print(-1/r)
print(float(-1/r))
print(int(r))
print(Rational(10,3)*Rational(101,8)-Rational(11,8))
# print(Rational(10,8) < Rational(10,9))
print(sorted([Rational(10,3),Rational(9,8), Rational(10,1), Rational(1,100)]))
print(Rational(10,8)==Rational(5,4))
print(Rational(100,10))
print(-Rational(12345,128191) + Rational(101,103) * 30 / 44)
"""


