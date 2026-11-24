"""error_estimado_interpolacion — cuaderno 01.

Libro: ecuación (18.18).  Rn = f[x_{n+1},...,x_0] * prod(x - x_i)
"""

def error_estimado_interpolacion(dif_siguiente, nodos, x):
    """Estima el error de truncamiento con un punto extra.

    dif_siguiente : diferencia dividida de orden n+1.
    nodos         : lista x0 ... xn.
    x             : punto donde se evalúa.
    """
    producto = 1.0
    for xi in nodos:
        producto *= (x - xi)
    return dif_siguiente * producto


if __name__ == "__main__":
    # dif = 0.007865529, nodos (1,4,6), x = 2  ->  0.0629242
    print(error_estimado_interpolacion(0.007865529, [1, 4, 6], 2))
