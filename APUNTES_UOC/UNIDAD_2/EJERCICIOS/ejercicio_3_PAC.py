"""
ejercicio 3 de la PAC
Jluis 16/10/21
"""
a = int(input("Escribe la variable a:  "))
b = int(input("Escribe la variable b:  "))
c = int(input("Escribe la variable c:  "))
variable_b = b*(-1)
b_2 = b * b
producto_ac = 4 * a * c
variable_a = 2 * a
resultado_bac = b_2 - producto_ac
resultado_numerador = variable_b + pow(resultado_bac,0.5)
resultado_total = resultado_numerador / variable_a
print(resultado_total)
