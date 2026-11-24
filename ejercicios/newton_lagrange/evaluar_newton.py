"""evaluar_newton — cuaderno 02.

Libro: ecuación (18.7), evaluada con Horner.
"""

def evaluar_newton(coef, x, xx):
    n = len(coef)
    p = coef[n - 1]
    for k in range(n - 2, -1, -1):
        p = p * (xx - x[k]) + coef[k]
    return p


if __name__ == "__main__":
    print(evaluar_newton([1, 4, 6], [0, 0.4620981, -0.0518731], 2))
    # esperado: 0.5658444
