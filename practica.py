"""practica de slicing dia 10"""

import os


def limpiar_pantalla():
    """
    Docstring for limpiar_pantalla
    """
    os.system("cls")


# mostar el ultimo valor del tuplas


def ejercicio_palindromos():
    """
    Docstring for ejercicio_palindromos
    """
    palabras = ("oso", "radar", "ana", "historia", "perro")

    palabra = palabras[0]

    es_palindromo = palabra == palabra[::-1]

    print(f"La palabra oso es palindromo ?: {es_palindromo}")

    # radar
    palabras_dos = palabras[1]
    es_palindromo2 = palabras_dos == palabras_dos[::-1]
    print(f"La palabra radar es palindromo ?: {es_palindromo2}")

    # ana
    palabras_tres = palabras[2]
    es_palindromo_tres = palabras_tres == palabras_tres[::-1]
    print(f"La palabra ana es palindromo ?: {es_palindromo_tres}")

    # historia
    palabras_cuatro = palabras[-2]
    es_palindromo_cuatro = palabras_cuatro == palabras_cuatro[::-1]
    print(f"La palabra historia es palindromo?: {es_palindromo_cuatro}")

    # perro
    palabras_cinco = palabras[-1]
    es_palindromo_cinco = palabras_cinco == palabras_cinco[::-1]
    print(f"La palabra perro es palindromo>?: {es_palindromo_cinco}")
    print(" ")


def ejericio_palindromo_dos():
    """
    Docstring for ejericio palindromo 2
    """

    palabras = ("Ana", "OSO", "RadaR", "Python")
    palabra = palabras[0]
    palindromo1 = palabra == palabra[::-1]

    print(f"La palabra 'Ana' es palindromo ?: {palindromo1}")

    # OSO
    palabra2 = palabras[1]
    palindromo2 = palabra2 == palabra2[::-1]

    print(f"La palabra 'OSO' es palindromo?: {palindromo2}")

    # Radar
    palabra3 = palabras[-2]
    palindromo3 = palabra3 == palabra3[::-1]
    print(f"La palabra 'RadaR' es palindromo?: {palindromo3}")

    # python
    palabras4 = palabras[-1]
    palindrimo4 = palabras4 == palabras4[::-1]
    print(f"La palabra 'python' es palindromo?: {palindrimo4}")


def ejericio_palindromo_tes():
    """
    Docstring for ejericio palindromo tes
    """

    palabras = ("anita lava la tina", "amor a roma", "somos o no somos", "radar civil")
    palabra = palabras[0]
    palindromo = palabra == palabra[::-1]
    print(f"La palabra 'anita lava la tina.' es palindromo?: {palindromo}")

    # amor a roma.
    palabra2 = palabras[1]
    palindromo2 = palabra2 == palabra2[::-1]
    print(f"La palabra 'amor a roma' es palindromo?: {palindromo2}")

    # somos o no somos
    palabra3 = palabras[-2]
    palindromo3 = palabra3 == palabra3[::-1]
    print(f"La palabra 'somos o no somos' es palindromo?: {palindromo3}")

    # radar civil

    palabras4 = palabra[-1]
    palindromo4 = palabras4 == palabras4[::-1]
    print(f"La palabra 'radar civil' es palindromo?: {palindromo4}")


def ejercicio_palindromo_cuatro():
    """
    Docstring for ejercicio palindromo cuatro
    """
    palabras = ("seres", "reconocer", "aja", "oso", "accion")

    palabra = palabras[0]
    palindromo = palabra == palabra[::-1]
    print(f"La palabra 'seres' es palindromo?: {palindromo}")

    # reconocer

    palabra2 = palabras[1]
    palindromo2 = palabra2 == palabra2[::-1]
    print(f"La palabra 'reconocer' se palindromo?: {palindromo2} ")

    # aja
    palabra3 = palabras[-3]
    palindromo3 = palabra3 == palabra3[::-1]
    print(f"la palabra 'aja' es palindromo?: {palindromo3}")

    # oso
    palabra4 = palabras[-2]
    palindromo4 = palabra4 == palabra4[::-1]
    print(f"La palabra 'oso' se palindromo?: {palindromo4}")

    # accion
    palabra5 = palabras[-1]
    palindromo5 = palabra5 == palabra5[::-1]
    print(f"La palabra 'accion' es palindromo?: {palindromo5}")


def ejercicio_menu():
    """
    Docstring para menu de ejericios.
    """

    while True:
        try:
            limpiar_pantalla()
            print("======MENU DE EJERICIO======")
            print("Ingrese la opcion deseada.")
            print("1. Ejercicio uno.")
            print("2. Ejercicio dos.")
            print("3. Ejercicio tres.")
            print("4. Ejercicio cuatro.")
            print("5. Salir.")
            menu = int(input("que desea ver toquel el numero deseado: "))

            if menu == 1:
                while True:
                    try:
                        limpiar_pantalla()

                        print("has ingresado a ejericio 1.")
                        print("1. Desea seguir ?.")
                        print("2. Regresar.")
                        submenu = int(input("ingrese la opcion deseada: "))

                        if submenu == 1:
                            ejercicio_palindromos()
                            input("Toque 'Enter' para seguir.")
                        elif submenu == 2:
                            print("Regresando al menu.")
                            input("Toque 'Enter' terminar.")
                            limpiar_pantalla()

                            break
                        else:
                            print("has ingresado una opcion invalida.")
                            input("Toque 'Enter' para seguir.")

                    except ValueError:
                        print("Saliendo del programa.")
                        input("Toque 'Enter' para seguir.")

            elif menu == 2:
                while True:
                    try:
                        limpiar_pantalla()
                        print("has ingresado a ejercicio 2.")
                        print("1. Desea seguir?.")
                        print("2. Regresar.")
                        submenu_dos = int(input("ingrese la opcion deseada: "))

                        if submenu_dos == 1:
                            ejericio_palindromo_dos()
                            input("Toque 'ENTER' para terminar.")
                            break
                        elif submenu_dos == 2:
                            print("Regreando al menu.")
                            input("Toque 'Enter' para segur.")
                            limpiar_pantalla()
                            break
                        else:
                            print("has ingresado una opcion invalida.")
                            input("Toque 'Enter' para seguir.")

                    except ValueError:
                        print("Saliendo del programa.")
                        input("Toque 'Enter' para seguir.")

            elif menu == 3:
                while True:
                    try:
                        limpiar_pantalla()
                        print("has ingresado a ejercicio 3.")
                        print("1. Desea seguir?.")
                        print("2. Regresar.")
                        submenu_tres = int(input("ingrese la opcion deseada: "))

                        if submenu_tres == 1:
                            ejericio_palindromo_tes()
                            input("Toque 'ENTER' para terminar.")
                            break

                        elif submenu_tres == 2:
                            print("Regreando al menu.")
                            input("Toque 'Enter' para terminar.")
                            limpiar_pantalla()
                            break
                        else:
                            print("has ingresado una opcion invalida.")
                            input("Toque 'Enter' para seguir.")

                    except ValueError:
                        print("ERROR, has ingresado una letra.")
                        input("Toque 'Enter' para seguir.")

            elif menu == 4:
                while True:
                    try:
                        limpiar_pantalla()
                        print("has ingresado a ejercicio 4.")
                        print("1. Desea seguir?.")
                        print("2. Regresar.")
                        submenu_cuatro = int(input(" ingrese la opcion deseada: "))

                        if submenu_cuatro == 1:
                            ejercicio_palindromo_cuatro()
                            input("Toque 'Enter' para terminar.")
                            break

                        elif submenu_cuatro == 2:
                            print("saliendo del programa.")
                            input("Toque 'Enter' para seguir.")
                            limpiar_pantalla()

                            break
                        else:
                            print("has ingresado una opcion invalida.")
                            input("Toque 'Enter' para seguir.")

                    except ValueError:
                        print("Error, has ingresado una letra.")
                        input("Toque 'Enter' para seguir.")

            elif menu == 5:
                print("Saliendo del programa.")
                input("Toque 'Enter' para seguir.")
                break
            else:
                print("Has ingresado una opcion no disponible.")
                input("Toque 'Enter' para seguir.")

        except ValueError:
            print("ERROR, has ingresado una letra.")
            input("Toque 'Enter' para seguir.")


ejercicio_menu()
