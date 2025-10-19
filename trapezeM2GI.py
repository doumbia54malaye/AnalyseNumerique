import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

def trapeze(a, b, n, function):
    x = sp.Symbol('x')
    f = sp.lambdify(x, function, 'numpy')
    h = (b-a)/n
    xi = np.zeros(n)
    som = f(a) + f(b)
    
    for i in range(1, n):
        xi = a + i*h
        som += 2*f(xi)  
    I = (h/2) * som
    
    return I