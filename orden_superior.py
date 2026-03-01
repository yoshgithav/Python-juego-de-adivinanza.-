"""
count,strip,sorted,sort,raise,index,extendm,(items,values,keys,clear,del,fromkeys) get,update:actualiza, setdefaul actualiza nuevo, pero no lo que existe.
"""

"""
add
"""



try:
    with open("text.txt") as file:
        print(file.read())

    print(file.closed)
except ValueError:
    print("error el archivo no existe")
