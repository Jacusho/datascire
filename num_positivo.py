"""
jluis
26/09/21
"""
# Suponiendo que el usuario solo pone numeros
a = int(input("Escribe un número positivo:  "))
while a <0:
    print("Te has equivocado. Intentalo de nuevo.")
    a = int(input("Escribe un número positivo:  "))

