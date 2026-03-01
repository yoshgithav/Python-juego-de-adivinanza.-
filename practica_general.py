"""
Docstring for practica_general
"""

try:
    user = input("Enter your user: ")
    password = input("Enter your password: ")

    if user == "admin" and password == "1234":
        print("Acceso Permitido.")
    else:
        raise ValueError("credenciales incocrrectas")

except ValueError as e:
    print(f"error: {e}")
    
