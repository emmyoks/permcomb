# This is a permutation module.
# This module returns the permutation of the integer or string entered as a variable
# This module requires only one variable , a sting or an integer
def fac(n):
    # if variable n is a string
    if n==str(n):
        n=len(n)
    else:
        i = 0
        m = 1
        for y in range(n - 1):
            i += 1
            m += i * (m)
    i=0
    m=1
    for y in range(n-1):
        i+=1
        m+=i*(m)
    return m
# This is a combination module.
# This module returns the Combination of the integer or string entered as the first variable.
# This module requires two variable , a sting or an int for the first variable and the second variable must be an int
def comb(n,r):
    if type(r)!= int:
        raise TypeError("The second varible r must be an integer")
    if n==str(n):
        if r > len(n):
            raise ValueError("The value of second variable 'r' shouldn't be greater than the length of the first variable 'n'.")
        n=len(n)
    else:
        if r > n:
            raise ValueError("The value of second variable 'r' shouldn't be greater than the value of first variable 'n' .")
        d = n - r
        combr = fac(n) / (fac(r) * fac(d))
        return combr
    d=n-r
    combr=fac(n)/(fac(r)*fac(d))
    return str(combr)


                 # test
        # from itertools import combinations as comb
        # from itertools import permutations as perm
        # import permcomb
        # l='abc'
        # print(permcomb.fac(l))
        # per=[''.join(p) for p in perm(l)]
        # print(per)
        # print(permcomb.comb(l,2))
        # com=[''.join(p) for p in comb(l,2)]
        # print(com)