import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def rectangle(a, b, n,function):
    h = (b-a)/n
    S = 0
    x = sp.Symbol('x')
    f = sp.lambdify(x, function, 'numpy')
    for i in range(n):  
        x_i = a + i * h 
        S += f(x_i)
    I = h * S
    return I