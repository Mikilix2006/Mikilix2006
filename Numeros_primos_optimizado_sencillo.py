import math

cont = 2
vueltas = 0

min = int(input("Escribe el número mínimo desde el que quieres que se muestren los primos (del 3 para arriba elige cualquier número, obviando el 2): "))
max = int(input("Escribe el número máximo hasta el que quieres que se muestren los primos: "))

if min > max:
    print("El número máximo tiene que ser más alto que el mínimo")
else:
    if min <= 0 or max <= 0:
        print("Solo se admiten números superiores al 0")
    else:
        if min == 1:
            print("El 1 no es primo, introduce números mayores al 1")
        else:
            if min == 2:
                print("Vamos a obviar que el 2 es primo para que el codigo funcione, gracias")
            else:
                print("Lista de primos:")
                while min + vueltas <= max:
                    modulo = (min + vueltas) % cont
                    if modulo == 0:
                        cont = 2
                        vueltas = vueltas + 1
                    if modulo != 0:
                        if cont >= math.sqrt(min):
                            print(min + vueltas)
                            cont = 1
                            vueltas = vueltas + 1
                        cont = cont + 1
