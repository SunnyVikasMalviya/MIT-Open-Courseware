from math import factorial

def catalan(n) :
    """
    Catalan numbers are a sequence of natural numbers that occurs in many
    interesting counting problems like counting the number of :
    1. full binary tree with exactly n internal nodes.
    2. expressions n pairs patenthesis which are correctly matched.
    3. full binary trees with n+1 leaves.
    4. possible binary search trees with n keys.
    """
    res = factorial(2*n)//(factorial(n+1)*factorial(n))
    return res


if __name__ == "__main__" :
    print(catalan(0))
    print(catalan(1))
    print(catalan(2))
    print(catalan(3))
    print(catalan(4))



"""
INPUT

0
1
2
3
4

OUTPUT

1
1
2
5
14

"""
