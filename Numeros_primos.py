import sys

def division():
    global der 
    global izq 

    while der != 0:
        if izq == 2:
            print(izq)
            der = 0
        valor = izq % der
        der = der - 1 
        if valor == 0:
            der = 0
        if der == 1:
            print(izq)
            der = 0
    if izq == 1:
        print(izq, " no es primo")


#Comienza
max = int(input("Hasta qué número quieres que calcule sus primos? (Calcular todos los primos: poner número menor a 2):  "))
start = int(input("Desde qué número quieres empezar?:  "))
if start <= 1:
    if start < 0:
        print("No se admiten negativos")
        sys.exit()
    start = start - 1
    print("Los primos son:")
    print("2")
if start >= 1:
    start = start - 4
    print("Los primos son:")


izq = 3 + start
der = izq - 1 + start

while izq != max + 1:
    '''izq != 10'''
    division()
    izq = izq + 1 
    der = izq - 1 
