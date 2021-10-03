
"""
Jluis
02/10/21
"""

numeros = [1,2,3,4,5,6,7,8,9,10]
numeros2 = []

print(numeros)
while numeros[-1] != 6:
    del numeros[-1]
numeros1 = numeros
print(numeros1)

for num in numeros:
    if num%2 == 0:
        numeros2.append(num)
print(numeros2)
