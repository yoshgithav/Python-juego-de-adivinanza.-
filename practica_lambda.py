def practica_lambda():
    """
    uso del lambda
    """

    def retonar_nota(estudiantes):
        """
        proceso de hacer lambda
        """
        # aqui se usa lambda seria key=lambda x: x[1]
        return estudiantes[1]

    listas_nombres = [
        ("Carlos", 8.5),
        ("María", 4.2),
        ("José", 9.1),
        ("Ana", 7.0),
        ("Luis", 5.5),
        ("Carmen", 7.8),
        ("Pedro", 4.7),
    ]
    # lista_ordenada = sorted(listas_nombres, key=lambda x:x[1])
    lista_ordenada = sorted(listas_nombres, key=retonar_nota)
    print(lista_ordenada)


def practica_lambda2():
    """
    Practica de lambda procesos.
    """
    listas_nombres = [
        ("Carlos", 8.5),
        ("María", 4.2),
        ("José", 9.1),
        ("Ana", 7.0),
        ("Luis", 5.5),
        ("Carmen", 7.8),
        ("Pedro", 4.7),
    ]

    acomodar_listas = sorted(listas_nombres, key=lambda x: x[1])
    print(acomodar_listas)


practica_lambda2()
