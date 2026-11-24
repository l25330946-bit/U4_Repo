"""error_newton — cuaderno 02.

Libro: ecuación (18.19).  R = b_n * prod_{i<n}(x - x_i)
"""

def error_newton(x, coef, xx):
    """Estima el error del polinomio de Newton en ``xx``."""
    n = len(coef) - 1          # índice del último coeficiente, b_n
    producto = 1.0
    for i in range(n):         # i < n: el último nodo no entra
        producto *= (xx - x[i])
    return coef[n] * producto


if __name__ == "__main__":
    print(error_newton([1, 4, 6, 5], [0, 0.4620981, -0.0518731, 0.007865529], 2))
    # esperado: 0.0629242
