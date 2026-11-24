"""interpolacion_lagrange — cuaderno 02.

Libro: ecuaciones (18.20) y (18.21).
"""

def interpolacion_lagrange(x, y, xx):
    """Evalúa el polinomio de Lagrange en ``xx``."""
    n = len(x)
    suma = 0.0
    for i in range(n):
        # Peso L_i(xx), ecuación (18.21)
        L = 1.0
        for j in range(n):
            if j != i:
                L *= (xx - x[j]) / (x[i] - x[j])
        # Término de (18.20)
        suma += L * y[i]
    return suma


if __name__ == "__main__":
    print(interpolacion_lagrange([1, 4, 6], [0, 1.386294, 1.791759], 2))
    # esperado: 0.5658444 (el mismo polinomio que Newton)
