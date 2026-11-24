"""interpolacion_newton — cuaderno 02.

Método completo: coeficientes + evaluación.
"""

from ejercicios.newton_lagrange.coeficientes_newton import coeficientes_newton
from ejercicios.newton_lagrange.evaluar_newton import evaluar_newton


def interpolacion_newton(x, y, xx):
    """Interpola con el polinomio de Newton en ``xx``."""
    coef = coeficientes_newton(x, y)
    return evaluar_newton(coef, x, xx)


if __name__ == "__main__":
    print(interpolacion_newton([1, 4, 6], [0, 1.386294, 1.791759], 2))
    # esperado: 0.5658444
