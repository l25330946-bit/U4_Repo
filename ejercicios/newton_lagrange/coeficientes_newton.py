"""coeficientes_newton — cuaderno 02.

Libro: ecuaciones (18.8) a (18.11). Llama a ``tabla_diferencias``.
"""

from ejercicios.newton_lagrange.tabla_diferencias import tabla_diferencias


def coeficientes_newton(x, y):
    T = tabla_diferencias(x, y)
    return [T[k][k] for k in range(len(x))]


if __name__ == "__main__":
    print(coeficientes_newton([1, 4, 6], [0, 1.386294, 1.791759]))
    # esperado: [0, 0.4620981, -0.0518731]
