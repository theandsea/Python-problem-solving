class Interval(object):
    def __init__(self, a, b):
        """
        :a: integer
        :b: integer
        """
        assert a < b
        assert isinstance(a, int)
        assert isinstance(b, int)
        self._a = a
        self._b = b

    def __repr__(self): # report
        # Interval(1, 4)
        reprstr="Interval("+str(self._a)+","+str(self._b)+")"
        return reprstr

    def __eq__(self, other):
        assert isinstance(other,Interval)
        if self._a==other._a and self._b==other._b:
            return True
        else:
            return False

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __le__(self, other):
        pass

    def __add__(self, other):
        # if no overlap
        assert isinstance(other, Interval)
        if self._b <= other._a or other._b <= self._a:
            return [self,other]
        else:
            low = min(self._a,other._a)
            high = max(self._b,other._b)
            return Interval(low,high)

"""
a=Interval(1,3)
a1=Interval(1,3)
b=Interval(2,4)
c=Interval(5,10)
print(a+b)
print(b+c)
print(a==a1)
"""
