"""
autor jluis
26/09/21
"""
lista_1 = [1,2,3,4,5,6]
lista_2 = lista_1[0:4]#[1,2,3,4]
lista_3 = lista_2[1:3]#[2,3]
a = lista_2.pop(1)#[1,3,4]
b = lista_3.pop()#[2]fuera ultimo elemento
lista_4 = []
lista_4.append(a)
lista_4.append(b)
lista_4 == lista_3