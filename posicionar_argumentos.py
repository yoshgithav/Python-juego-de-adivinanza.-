"""
uso de argumentos en una funcion def
"""


# posicionar argumentos
def imprimir_nombres(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido):
    """
    definir posiciones del def
    """
    print(
        f"hola {primer_nombre} {segundo_nombre} "
        f"{primer_apellido } {segundo_apellido} "
        "bienvenido al curso de python"
    )


imprimir_nombres("carlos", "alberto", "rivera", "gonzalex")
# usar cntrol /
# keyword arguments
imprimir_nombres(
    segundo_apellido="gonzalex",
    primer_nombre="carlos",
    primer_apellido="rivera",
    segundo_nombre="alberto",
)

imprimir_nombres(
    "carlos", "albert", primer_apellido="rivera", segundo_apellido="gonzalex"
)


# iteralbe unpacking

estudiantes = ("carlos", "alberto", "gomez", "rojas")

imprimir_nombres(*estudiantes)


estudiantes_dict = {
    "primer_apellido": "rivera",
    "primer_nombre": "carlos",
    "segundo_nombre": "alberto",
    "segundo_apellido": "gonzalez",
}

imprimir_nombres(**estudiantes_dict)
