"""
Docstring  practicas_listas dia 15
"""

import os


def limpiar():
    """
    limpiar pantalla para el menu.
    """
    os.system("cls")


def ejercico_compras():
    """
    Docstring for ejercico_compras
    """
    productos = []
    precio = []

    primero = input("ingrese un producto: ")
    precio1 = float(input("ingrese el precio: "))

    segundo = input("ingrese el producto: ")
    precio2 = float(input("ingrese el precio: "))

    tercero = input("ingrese el producto: ")
    precio3 = float(input("ingrese el precio: "))

    productos = [primero, segundo, tercero]
    precio = [precio1, precio2, precio3]
    print(f"productos {productos}")

    nuevo_pro = input("ingrese el producto: ")
    nuevo_pre = float(input("ingrese el precio: "))
    posicion_nue = int(input("ingres la posicion: "))
    productos.insert(posicion_nue, nuevo_pro)
    precio.insert(posicion_nue, nuevo_pre)

    print(productos)

    quitar = int(input("ingres la posicion para eliminar: "))
    eliminar_pro = productos.pop(quitar)
    eliminar_pre = precio.pop(quitar)
    print(" ")

    print(productos)

    remplazar = input("ingrese el producto para remplazar: ")
    remplazar_pre = float(input("ingrese el precio: "))
    remplazar_posi = int(input("ingrese la posicion: "))
    productos[remplazar_posi] = remplazar
    precio[remplazar_posi] = remplazar_pre

    print(f"productos: {productos}, Precio: {precio}")
    print(f"Eliminados:{eliminar_pro}, Precio: {eliminar_pre}")
    print(f"total productos: {len(productos)}")
    print(f"total de compra: {sum(precio)}")


def ejercicio_notas():
    """
    Docstring for ejercicio_notas
    """

    notas = []

    nota1 = float(input("ingrese la nota: "))
    nota2 = float(input("ingrese la nota: "))
    nota3 = float(input("ingrese la nota: "))
    nota4 = float(input("ingrese la nota: "))

    notas = [nota1, nota2, nota3, nota4]

    nuevo = float(input("ingrese una nueva nota: "))
    posicion = int(input("ingrese la posicion: "))
    notas.insert(posicion, nuevo)
    print(notas)
    print(" ")

    quitar = int(input("ingrese la posicion para eliminar: "))
    eliminar = notas.pop(quitar)
    print(" ")

    print(notas)
    remplazar = float(input("ingrese la nota para remplazar: "))
    posicion_rem = int(input("ingrese la posicion: "))
    notas[posicion_rem] = remplazar

    print(f"Notas: {notas}")
    print(f"Eliminados {eliminar}")
    print(f"suma de las notas: {sum(notas)}")
    print(f"promedio {sum(notas) / len(notas)}")


def ejercicio_peliculas():
    """
    Docstring for ejercicio_peliculas
    """

    peliculas = []
    minutos = []

    primero = input("ingrese la pelicula: ")
    minutos1 = float(input("ingrese los minutos: "))

    segundo = input("ingrese la pelicula: ")
    minutos2 = float(input("ingrese el minuto: "))

    tercero = input("ingrese la pelicula: ")
    minutos3 = float(input("ingrese el minuto: "))

    peliculas = [primero, segundo, tercero]
    minutos = [minutos1, minutos2, minutos3]

    quitar = int(input("ingrese la posicion para eliminar: "))
    eliminar_peli = peliculas.pop(quitar)
    eliminar_minu = minutos.pop(quitar)

    remplazar = input("ingrese la nueva pelicula para remplazar: ")
    minutos_rem = float(input("ingrese el minuto: "))
    nuevo_posi = int(input("ingrese la posicion: "))
    peliculas[nuevo_posi] = remplazar
    minutos[nuevo_posi] = minutos_rem

    print(f"peliculas: {peliculas}")
    print(f"minutos en  total: {sum(minutos)}")
    print(f"peliculas eliminados: {eliminar_peli}, minutos: {eliminar_minu}")


def ejercicio_animales():
    """
    Docstring for ejercicio_animales
    """

    animales = []
    edades = []

    primero = input("ingrese un animal: ")
    edad1 = int(input("ingrese la edad: "))

    segundo = input("ingrese un animal: ")
    edad2 = int(input("ingrese la edad: "))

    tercero = input("ingrese un animal")
    edad3 = int(input("ingrese la edad: "))

    animales = [primero, segundo, tercero]
    edades = [edad1, edad2, edad3]

    print(f"animales: {animales}, edades: {edades}")

    quitar = int(input("ingre la posicion para eliminar: "))
    eliminar_animales = animales.pop(quitar)
    eliminar_edades = edades.pop(quitar)
    print(" ")

    remplazo = input("ingresa el animal para remplazar: ")
    remplazo_edad = int(input("ingres la edad: "))
    posicion_remplazo = int(input("ingresa la posicion: "))
    animales[posicion_remplazo] = remplazo
    edades[posicion_remplazo] = remplazo_edad

    print(f"lista de animales: {animales} y edad: {edades}")
    print(f"animales elimandos: {eliminar_animales}, edad: {eliminar_edades}")


def ejericio_tareas():
    """
    Docstring for ejericio_tareas
    """
    tarea = []
    tiempos = []

    tarea1 = input("ingresa la materia: ")
    tiempos1 = int(input("ingresa el tiempo: "))

    tarea2 = input("ingrese la materia: ")
    tiempos2 = int(input("ingrese el tiempo: "))

    tarea3 = input("ingrese la materia: ")
    tiempos3 = int(input("ingrese el tiempo: "))

    tarea = [tarea1, tarea2, tarea3]
    tiempos = [tiempos1, tiempos2, tiempos3]

    print(f"tarea: {tarea}, tiempo : {tiempos}")

    quitar = int(input("ingrese la posicion: "))
    eliminar_tarea = tarea.pop(quitar)
    eliminar_tiempo = tiempos.pop(quitar)

    print(tarea)

    remplazar = input("ingrese la tarea a remplazar: ")
    remplazar_tiempo = int(input("ingrese el tiempo: "))
    remplazar_posi = int(input("ingrese la posicion: "))
    tarea[remplazar_posi] = remplazar
    tiempos[remplazar_posi] = remplazar_tiempo

    print(f"lista de las materias: {tarea}, tiempos: {tiempos}")
    print(f"total de horas: {sum(tiempos):.2f}")
    print(f"materia eliminada: {eliminar_tarea}, tiempo: {eliminar_tiempo}")
