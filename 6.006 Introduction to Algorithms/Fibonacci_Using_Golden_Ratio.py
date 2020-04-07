def fib_g(n) :
    """
    The function fib_g is used to find the nth fibonacci number using the golden
    ratio i.e. 1.618033 by using the formula :
    
    fibonacci = (phi**n) / 5**(0.5).

    This results in a floating answer hence we use round function to round it
    off to the nearest integer.
    """
    phi = 1.618033
    res = round((phi**n)/(5**(0.5)))
    return res

if __name__ == '__main__' :
    print(fib_g(0))
    print(fib_g(1))
    print(fib_g(2))
    print(fib_g(3))
    print(fib_g(4))
    print(fib_g(5))
    print(fib_g(6))
    print(fib_g(7))
    print(fib_g(8))
    print(fib_g(9))
    print(fib_g(10))

"""
INPUT

0
1
2
3
4
5
6
7
8
9
10

OUTPUT

0
1
1
2
3
5
8
13
21
34
55
"""
