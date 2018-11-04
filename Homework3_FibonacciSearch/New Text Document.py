import math
f = lambda x: math.exp(1-x) + x**2

def F(n):
    if n == 0: 
        return 1
    elif n == 1: 
        return 1
    else: 
        return F(n-1)+F(n-2)
    
def FibSearch(f, a, b, tol=1e-6, n=20):
    gamma = F(n-2)/F(n)
    A0 = a + gamma*(b-a)
    B0 = b - gamma*(b-a)
    n = n-1
    while abs(b - a) > tol and n > 1:
        gamma = F(n-2)/F(n)
        n = n-1
        if f(A0) < f(B0):
            b = B0
            B1 = A0
            A1 = a + gamma*(b-a)
        else:
            a = A0
            A1 = B0
            B0 = b - gamma*(b-a)
    return (b-a)/2

FibSearch(f,0,2)