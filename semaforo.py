"""
autor Jluis 
programa semaforo 
11/09/21

"""
def semaforo():
    color_semaforo = ["rojo","ambar","verde"]
    color_usuario = input("Que color tiene el semaforo? :  ")
    if color_usuario == color_semaforo[0]:
        print(color_semaforo[0])
    elif color_usuario == color_semaforo[1]:
        print(color_semaforo[1])
    elif color_usuario == color_semaforo[2]:
        print(color_semaforo[2])
    else: 
        print("Te has equivocado, vuelve a intentarlo")
        return semaforo()

semaforo()       

