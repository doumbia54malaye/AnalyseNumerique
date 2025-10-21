import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
import time

def trapeze(a, b, n, function):
    t0_trap = time.perf_counter()
    x = sp.Symbol('x')
    f = sp.lambdify(x, function, 'numpy')
    h = (b-a)/n
    xi = np.zeros(n)
    som = f(a) + f(b)
    
    for i in range(1, n):
        xi = a + i*h
        som += 2*f(xi)  
    I = (h/2) * som
    tf_trap = time.perf_counter() - t0_trap
    return "Résultat M Trap : " + str(I) + " | Temps d'exécution : " + str(tf_trap)
