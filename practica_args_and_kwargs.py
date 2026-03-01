"""
practica
"""


def clientes_info(*args, **kwargs):
    """
    Practica de args y kwargs
    """
    subtotal = sum(args)

    descuento = kwargs.get("descuento", 0)
    impuesto = kwargs.get("impuesto", 0)
    envio = kwargs.get("envio", 0)
    cupon = kwargs.get("cupon", 0)
    cliente = kwargs.get("cliente", "desconocido")

    subtotal -= subtotal * descuento
    subtotal += subtotal * impuesto
    subtotal += envio
    subtotal -= cupon

    print(f"nombre {cliente} precio final: ${subtotal}")
    return subtotal


lista_precio = [56, 34, 85, 56]
dict_totales = {
    "descuento": 0.05,
    "impuesto": 0.07,
    "envio": 5,
    "cupon": 6,
}

total_todo = clientes_info(*lista_precio, **dict_totales)
for datos, totales in dict_totales.items():
    print(f"{datos:<10} ---> {totales}")
