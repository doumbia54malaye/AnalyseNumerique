def newton_raphson(f, f_prime, x0_initial, NMAX, epsilon):
    n = 0
    x_old = x0_initial
    
    x0 = x_old - f(x_old) / f_prime(x_old)  

    while abs(x0 - x_old) > epsilon and n < NMAX:
        n += 1
        x_old = x0

        if f_prime(x_old) == 0:
            print("Erreur : la dérivée en x ne doit pas être égale à 0.")
            return float('nan')

        x0 = x_old - f(x_old) / f_prime(x_old)

    if n == NMAX:
        print("Trop d'itérations")
        return float('nan')
    else:
        return x0
# Exemple d'utilisation 
def f(x):
    return x**2 - 2  

def f_prime(x):
    return 2*x

racine = newton_raphson(f, f_prime, x0_initial=1, NMAX=100, epsilon=1e-6)
print("Résultat :", racine)