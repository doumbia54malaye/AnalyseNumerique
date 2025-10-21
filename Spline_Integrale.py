import numpy as np
import sympy as sp
import time
from Simpson import simpson


x_sym = sp.Symbol('x')

def splineQuad(x, y, nb_point_int):
    n = len(x)
    z = np.zeros(n)

    # Initialisation de z[0]
    z[0] = 0  # dérivée initiale arbitraire

    # Calcul des z[i]
    for i in range(n - 1):
        z[i + 1] = (2 * (y[i + 1] - y[i]) / (x[i + 1] - x[i])) - z[i]

    # Coefficients de chaque polynôme du spline
    a = np.zeros(n - 1)
    b = np.zeros(n - 1)
    c = np.zeros(n - 1)

    integrales = []  # liste pour stocker les résultats
    total = 0        # somme totale des intégrales

    for i in range(n - 1):
        a[i] = (z[i + 1] - z[i]) / (2 * (x[i + 1] - x[i]))
        b[i] = z[i]
        c[i] = y[i]

        # Polynôme de spline local
        Si = a[i]*(x_sym - x[i])**2 + b[i]*(x_sym - x[i]) + c[i]

        # Calcul de l'intégrale par Simpson sur [x[i], x[i+1]]
        res = simpson(x[i], x[i + 1], nb_point_int, Si)

        integrales.append(res)
        total += float(res.split(':')[1].split('|')[0]) if isinstance(res, str) else res

        print(f"Spline S{i} sur [{x[i]}, {x[i+1]}] → {res}")

    print("\nIntégrale totale du spline sur [", x[0], ",", x[-1], "] :", total)
    