"""
Docstring for funciones_args
"""

# def suma(*args):
#     """
#     practica
#     """
#     resultado = 0
#     for element in args:
#         resultado += element
#     return resultado


# resultado = suma(2, 1, 4, 6)
# print(f"La suma es: {resultado}")


def conectar_bd(**kwargs):
    nombres = kwargs["nombres_bd"]

    user = kwargs["usuario"]
    password = kwargs["password"]
    port = kwargs["password"]
    dir_bd = kwargs["dir_bd"]

    print(f"conenctado con la base de datos {nombres}")
    print(f"Login with: {user} - {password}")


conectar_bd(
    nombres_bd="generico",
    usuario="root",
    password="1234",
    port=5002,
    dir_bd="10.25.47.3",
)


# def factura(**kwargs):
#     """
#     Practica factura.
#     """
#     cliente = kwargs["cliente"]
#     producto = kwargs["producto"]
#     precio = kwargs["precio"]
#     cantidad = kwargs["cantidad"]
#     print("-" * 14)
#     print(f"cliente: {cliente}")
#     print(f"producto: {producto}")
#     print(f"precio: ${precio}")
#     print(f"cantidad: {cantidad}")
#     print("-" * 14)
#     print(f"Total: {cantidad * precio:.2f}")


# factura(
#     cliente="kevin",
#     producto="jabon",
#     precio=0.85,
#     cantidad=10,
# )
