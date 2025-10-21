import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import time

def simpson(a, b, n, function):
    t0_simp = time.perf_counter()
    x = sp.Symbol('x')
    f = sp.lambdify(x, function, 'numpy')
    # n doit être pair.

    if n % 2 == 1:
        raise ValueError("n doit être pair pour la règle de Simpson")
    
    h = (b - a) / n
    S = f(a) + f(b)
    # termes impairs (4) et pairs (2)
    for i in range(1, n):
        xi = a + i * h
        if i % 2 == 1:
            S += 4.0 * f(xi)
        else:
            S += 2.0 * f(xi)
    tf_simp = time.perf_counter() - t0_simp
    return "Résultat M Simp : " + str((h / 3.0) * S) + " | Temps d'exécution : " + str(tf_simp)