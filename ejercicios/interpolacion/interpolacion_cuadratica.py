"""interpolacion_cuadratica — cuaderno 01.

Libro: ecuación (18.3) con los coeficientes (18.4) a (18.6), calculados con dos
pendientes:

    m1 = (y1 - y0) / (x1 - x0)
    m2 = (y2 - y1) / (x2 - x1)
    b0 = y0      b1 = m1      b2 = (m2 - m1) / (x2 - x0)

y después se evalúa la forma anidada
``f2(x) = b0 + b1(x-x0) + b2(x-x0)(x-x1)``.

Devuelve **dos** cosas: el valor interpolado y el error.
"""

from ejercicios.interpolacion.error_estimado_interpolacion import (
    error_estimado_interpolacion,
)


def interpolacion_cuadratica(x0, y0, x1, y1, x2, y2, x, x3=None, y3=None):
    """Devuelve ``(y, error)``.

    y     : valor interpolado con la parábola que pasa por los tres nodos.
    error : ``None`` si no hay cuarto dato; si lo hay,
            ``R2 = f[x3,x2,x1,x0] * (x - x0)(x - x1)(x - x2)``.
    """
    # Pendientes entre tramos consecutivos
    m1 = (y1 - y0) / (x1 - x0)
    m2 = (y2 - y1) / (x2 - x1)

    # Coeficientes (18.4), (18.5), (18.6)
    b0 = y0
    b1 = m1
    b2 = (m2 - m1) / (x2 - x0)

    # Forma anidada (18.3)
    y = b0 + b1 * (x - x0) + b2 * (x - x0) * (x - x1)

    # Error (18.18): solo si hay cuarto dato
    error = None
    if x3 is not None and y3 is not None:
        m3 = (y3 - y2) / (x3 - x2)                      # f[x3, x2]
        f_x3_x2_x1 = (m3 - m2) / (x3 - x1)              # f[x3, x2, x1]
        f_x3_x2_x1_x0 = (f_x3_x2_x1 - b2) / (x3 - x0)   # f[x3, x2, x1, x0]
        error = f_x3_x2_x1_x0 * (x - x0) * (x - x1) * (x - x2)

    return y, error


if __name__ == "__main__":
    # nodos (0,1), (1,3), (2,7); evaluar en 1.5  ->  (4.75, None)
    print(interpolacion_cuadratica(0, 1, 1, 3, 2, 7, 1.5))
    # con cuarto dato: además del valor, el error estimado
    print(interpolacion_cuadratica(0, 1, 1, 3, 2, 7, 1.5, x3=3, y3=13))
