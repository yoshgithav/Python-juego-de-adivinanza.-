"""
Docstring for argumentos_opcionales, “función del parámetros”,
"""

# def calcular_precio(productos, cantidad, precio, descuento=0):
#     precio_final = (cantidad * precio) * (1 - descuento)
#     print(f"El precio final de los productos es:{precio_final}")


# calcular_precio("camisa", 3, 20, 0.20)


def calcular_precio(productos, cantidad, precio, descuento=0):
    precio_final = (cantidad * precio) * (1 - descuento)
    return productos, cantidad, precio_final


# tuplas
nombre, cantidad, precio = precio_final = calcular_precio("tijera", 3, 10)
print(nombre)
print(cantidad)
print(precio)
