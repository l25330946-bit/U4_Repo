"""interpolacion_lineal — cuaderno 01.

Libro: ecuación (18.2). Recta por dos nodos, evaluada en ``x``.

La función devuelve **dos** cosas: el valor interpolado y el error. El error es
``None`` cuando no se da un tercer dato; si se da, se estima con (18.18).
"""

from ejercicios.interpolacion.error_estimado_interpolacion import (
    error_estimado_interpolacion,
)


def interpolacion_lineal(x0, y0, x1, y1, x, x2=None, y2=None):
    """Devuelve ``(y, error)``."""
    # Ecuación (18.2): recta por (x0, y0) y (x1, y1)
    pendiente = (y1 - y0) / (x1 - x0)
    y = y0 + pendiente * (x - x0)

    # Error (18.18): solo si hay tercer dato
    error = None
    if x2 is not None and y2 is not None:
        f_x2_x1 = (y2 - y1) / (x2 - x1)           # f[x2, x1]
        f_x1_x0 = pendiente                        # f[x1, x0]
        f_x2_x1_x0 = (f_x2_x1 - f_x1_x0) / (x2 - x0)  # f[x2, x1, x0]
        error = f_x2_x1_x0 * (x - x0) * (x - x1)

    return y, error


if __name__ == "__main__":
    # sin tercer dato: f(1)=0, f(4)=3  ->  (1.0, None)
    print(interpolacion_lineal(1, 0, 4, 3, 2))
    # con tercer dato: además del valor, el error estimado
    print(interpolacion_lineal(1, 0, 4, 3, 2, x2=6, y2=5))
