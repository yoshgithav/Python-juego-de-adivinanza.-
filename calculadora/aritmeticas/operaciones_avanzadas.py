"""
operaciones_avanzanda
"""


def multi(a, b):
    "multiplicacion"
    return a * b


def divi(a, b):
    """
    division
    """
    try:
        return round(a / b, 2)
    except ZeroDivisionError:
        return "Resultado: error."
