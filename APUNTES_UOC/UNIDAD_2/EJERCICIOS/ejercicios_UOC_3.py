"""
Ejercicio UOC 3
Jluis 09/10/21
1. El último elemento de la primera lista
2. Una nueva lista con el primer elemento de cada una de las listas
3. Una nueva lista con los tres primeros elementos de la segunda lista
4. Una cadena de caracteres con el valor "Miércoles 8"
"""

l_1 = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
l_2 = [1, 2, 3, 4, 5, 6, 7, 8]

print(l_1[-1])
l_3 = []
l_3.append(l_1[0])
l_3.append(l_2[0])
print(l_3)
l_4 = []
for i in l_2[:3]:
    l_4.append(i)
print(l_4)
print(l_1[2] + " " + str(l_2[-1]))

