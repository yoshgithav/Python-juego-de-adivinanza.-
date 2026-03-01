"""
practica.
"""
import random as ra

import os

def limpiar():
    os.system("cls")

def juego_adivinanza():
    numero_secreto = ra.randint(1,10)
    intento = 0
    adivinados = False

    print("juego de adivinanzan del 1 al 100")

    while not adivinados:

        adivinanzas =input("ingrese un numero del 1 al 100: ")

        if adivinanzas.isdigit():
            adivinanzas = int(adivinanzas)
            intento += 1

            if adivinanzas < numero_secreto:
                print(f"el numero sercreto es mayor a {adivinanzas}")

            elif adivinanzas > numero_secreto:
                print(f"El numero secreto es menor a {adivinanzas}")
            else:
                print(f"has ganado el numero es {adivinanzas} intentos {intento}")
                break
        else:
            print("ingrese un numero valido del 1 al 100.")
            input("toca enter para seguir.")

#======================================================
def juego_adivinanzas1():
    numero_secreto = 5
    intentos = 0

    while True:
        try:
            print("Adivinanza del 1 al 10.")
            numero = int(input("ingrese un numero: "))

            if numero < 1 or numero > 10:
                print("el numero debe ser del 1 al 10.")
                continue

            intentos += 1

            if numero < numero_secreto:
                print("casi pero no, es mayor el numero.")

            elif numero > numero_secreto:
                print("casi, pero es menor el numero jejeje.")

            else:
                print(f"has ganado el numero secreto es: {numero_secreto} intentos {intentos}")
                break
        except ValueError:
            print("ingrese numero del 1 al 10.")

#======================================================
def juego_adivinanza2(minimo,maximo):

    numero_secreto = 5
    intentos = 0

    while True:
        try:
            print(f"==== Adivinanza del {minimo} al {maximo} ====")
            num = int(input(f"ingrese numero del {minimo} al {maximo}: "))

            if num < minimo or num >maximo:
                print(f"!ingrese solo numero del {minimo} al {maximo}!")
                input("Toca 'Enter' para seguir.")
                limpiar()
                continue

            intentos += 1

            if num < numero_secreto:
                print("casi el numero es mayor.")
                input("Toca 'Enter' para seguir.")
                limpiar()

            elif num > numero_secreto:
                print("casi el numero es menor.")
                input("Toca 'Enter' para seguir.")
                limpiar()

            else:
                print(f"has adivinado el numero secreto es:{num} ")
                print(f"intentados realizados {intentos}")
                break

        except ValueError:
            print(f"ingrese un numero por favor del {minimo} al {maximo}")
            input("Toca 'Enter' para seguir.")
            limpiar()

juego_adivinanza2(1,10)
