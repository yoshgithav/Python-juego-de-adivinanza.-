"""
sorted,sort,raise,index,extendm,(items,values,keys,clear,del,fromkeys) get,update:actualiza, setdefaul actualiza nuevo, pero no lo que existe.
"""

# list = ["a", "b" ,"B", "c", "e", "f","A"]

# print(list)
# eliminar = input("ingrese la letra a eliminar: ")

# new_list =[i for i in list if i.lower() != eliminar.lower()]
def practica():
    """
    Docstring for practica
    """
    numeros = [1,2,3,4,5,6,7,8,9,10]

    print(f"Lista de numeros: {numeros}")

    eliminados = []
    eliminados.append(numeros.pop(1))
    eliminados.append(numeros.pop(2))

    eliminados.append(numeros.pop(5))
    print(numeros)
    print(eliminados)

def practica_list():

    """
    uso del 'list' en python
    """
    #PRUEBA 1
    print(range(1,100,10))
    numeros = range(1,100,10)
    print(numeros)

    #usar list
    print(list(range(0,100,10)))

    nombre = "gato"
    print(list(nombre))

    lista_nombres = list(nombre)
    print(lista_nombres[::-1])
