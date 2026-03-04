"""
juego
"""
import os
import random as ra

def limpiar_pantalla() -> None:
    os.system("cls")

def obtener_palabras() -> str:
    palabras_secretas = ["relampago","algoritmo","horizonte","cuspide",
    "bitacora","entropía","nebulosa","mosaico","viaducto","quimera"]
    return ra.choice(palabras_secretas)

def mostrar_bienvenidos(intentos: int) -> None:
    print("Bienvenido al juego de ahorcado.")
    print(f"Tienes {intentos} intentos para adivinar la palabra.")
    print()

def mostrar_proceso(palabras_secretas,letras_adinivadas):
    adivinados = ""
    for letra in palabras_secretas:
        if letra in letras_adinivadas:
            adivinados += letra
        else:
            adivinados += "-"
    return f"Palabra: {adivinados}"

def configuracion_inicio():
    palabra_secreta = obtener_palabras()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    limpiar_pantalla()
    mostrar_bienvenidos(intentos)
    while not juego_terminado and intentos > 0:
        progreso_actual = mostrar_proceso(palabra_secreta,letras_adivinadas)
        print(progreso_actual)

        adivinanzas = input("ingrese una letra: ").lower().strip()

        if len(adivinanzas) != 1 or not adivinanzas.isalpha():
            print("ingrese letras por favor. ")
        elif adivinanzas in letras_adivinadas:
            print("ya has ingresado esta letra, intente de nuevo.")
        else:
            letras_adivinadas.append(adivinanzas)

            if adivinanzas in palabra_secreta:
                print(f"se ha encontrado la letra {adivinanzas}")
            else:
                intentos -= 1
                print(f"no se encontra le letra, intentos restantes: {intentos}.")

        if "-" not in progreso_actual:
            juego_terminado = True
            print(f"has ganado felicidades la palabra era {palabra_secreta}")

    if intentos == 0:
        print(f"has perdido.... la palabra secreta era {palabra_secreta}")

configuracion_inicio()
