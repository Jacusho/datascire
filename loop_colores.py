"""
autor jluis
19/09/21
"""

lista_1 = ["rojo","azul","verde","amarillo"]
lista_2 = ["gris", "verde", "negro", "azul"]
for color2 in lista_2:
    for color1 in lista_1:
        if color2 == color1:
            print(color2)
