import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def newton(f, f_prime, x0, epsilon=1e-6, Nmax=100):
    x = x0
    for i in range(Nmax):
        fx = f(x)
        fpx = f_prime(x)

        if fpx == 0:
            print("Erreur : dérivée nulle, impossible de continuer.")
            return None

        x_new = x - fx / fpx

        if abs(x_new - x) < epsilon:
            print(f"Convergence atteinte après {i+1} itérations.")
            return x_new

        x = x_new

    print("Aucune convergence après", Nmax, "itérations.")
    return x
