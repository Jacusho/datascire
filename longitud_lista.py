"""
autor jluis
26/09/21
"""
def lista(a):
    if type(a) == list:
        print(str(a) + " es una lista")
        if len(a) < 5:
            print(str(a) + " la lista es pequeña")
        else:
            print(str(a) + " la lista es grande")

    else:
        print(str(a) + " no es una lista")

