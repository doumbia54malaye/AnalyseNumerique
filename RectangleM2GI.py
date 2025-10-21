import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import time

def rectangle(a, b, n,function):
    t0_rec =time.perf_counter()
    h = (b-a)/n
    S = 0
    x = sp.Symbol('x')
    f = sp.lambdify(x, function, 'numpy')
    for i in range(n):  
        x_i = a + i * h 
        S += f(x_i)
    I = h * S
    tf_rec = time.perf_counter() - t0_rec
    return "Résultat M Rect : " + str(I) + " | Temps d'exécution : " + str(tf_rec) 