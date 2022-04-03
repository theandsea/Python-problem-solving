def fibonacci(n):
    """
    a generator to compute the first n Fibonacci numbers
    :param n:
    :return:
    """
    assert isinstance(n,int) and n>0
    yield 1
    if n<=1:
        return
    yield 1
    if n<=2:
        return
    a=1
    b=1
    for i in range(n-2):
        a = a+b
        a,b=b,a
        yield b

"""
print(list(fibonacci(1)))
print(list(fibonacci(2)))
print(list(fibonacci(3)))
print(list(fibonacci(10)))
"""
