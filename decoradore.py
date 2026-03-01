"""
poo.decoradore
"""
def El_coche(funcion):
    def coche_modificacion():
        print("me subi al coche.")
        funcion()
        print("me baje del coche.")
    return coche_modificacion

@El_coche
def viajar():
    print("estoy conduciendo por la ciudad.")

viajar()
