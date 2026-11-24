"""tabla_diferencias — cuaderno 02.

Libro: ecuaciones (18.12) a (18.14). La diagonal son los coeficientes b.
"""

def tabla_diferencias(x, y):
    """Devuelve la tabla n x n como lista de listas (rellenada con ceros).

    T[i][0] = y[i]
    T[i][j] = (T[i][j-1] - T[i-1][j-1]) / (x[i] - x[i-j])
    """
    n = len(x)
    T = [[0.0] * n for _ in range(n)]

    for i in range(n):
        T[i][0] = y[i]

    for j in range(1, n):
        for i in range(j, n):
            T[i][j] = (T[i][j-1] - T[i-1][j-1]) / (x[i] - x[i-j])

    return T


def coeficientes_newton(x, y):
    """Devuelve la diagonal de la tabla: b0, b1, ..., bn."""
    T = tabla_diferencias(x, y)
    return [T[k][k] for k in range(len(x))]


if __name__ == "__main__":
    T = tabla_diferencias([1, 4, 6], [0, 1.386294, 1.791759])
    for fila in T:
        print(fila)
    # diagonal esperada: 0, 0.4620981, -0.0518731
