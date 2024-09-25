import random
import time
import sys

rocasquitar = [1, 2, 3]
cantjugadores = [1, 2]    
total = random.randint(23,30)
jugando1 = True
jugando2 = True

#FUNCIÓN JUGAR IA
def IA ():
    global total
    print("La IA está pensando...")
    time.sleep(2)
    quitar = random.randint(1,3)
    total = total - quitar
    print("La IA ha quitado ", quitar, " roca/s")
    time.sleep(1)
    if total <= 0:
            print("La IA ha quitado la última piedra, has ganado. Resetea el programa.")
            sys.exit()
    return (total)

#FUNCIÓN JUGAR SOLO
def JUGADOR ():
    global total
    correcto = True
    
    while correcto:
        quitar = int(input("Elige el número de rocas que quitar entre 1 y 3: "))
        if quitar in rocasquitar:
            total = total - quitar
            correcto = False
            if total <= 0:
                print("Has quitado la última piedra, has perdido.\nResetea el programa.")
                sys.exit()
        
        if quitar < 1:
            print("Ese no es un número entre 1 y 3")
            correcto = True
        if 3 < quitar:
            print("Ese no es un número entre 1 y 3")
            correcto = True
    return (total)

#COMIENZA EL JUEGO
jugadores = int(input("¿Cuantos vais a jugar? (1 o 2): "))

if jugadores == 1:
    while jugando1:
        JUGADOR()   
        IA()
        

        
if jugadores == 2:
    nom1 = input("Jugador 1, introduce tu nombre: ")
    print("Hola ", nom1)
    nom2 = input("Jugador 2, introduce tu nombre: ")
    print("Hola ", nom2)
    
    #FUNCIÓN JUGADOR 1
    def JUGADOR1 ():
        global total
        global nom1
        correcto = True
        
        while correcto:
            quitar = int(input(nom1 + ", elige el número de rocas que quitar entre 1 y 3: "))
            if quitar in rocasquitar:
                total = total - quitar
                correcto = False
                print(nom1 + " ha quitado ", quitar, " piedra/s")
                time.sleep(1)
                if total <= 0:
                    print("Fin del juego")
                    time.sleep(1)
                    print(nom1 + " ha quitado la última piedra, ", nom1 + " ha perdido.\nResetead el programa.")
                    sys.exit()
            
            if quitar < 1:
                print("Ese no es un número entre 1 y 3")
                correcto = True
            if 3 < quitar:
                print("Ese no es un número entre 1 y 3")
                correcto = True
        return (total)

    #FUNCIÓN JUGADOR 2
    def JUGADOR2 ():
        global total
        global nom1
        correcto = True
        
        while correcto:
            quitar = int(input(nom2 + ", elige el número de rocas que quitar entre 1 y 3: "))
            if quitar in rocasquitar:
                total = total - quitar
                correcto = False
                print(nom2 + " ha quitado ", quitar, " piedra/s")
                time.sleep(1)
                if total <= 0:
                    print("Fin del juego")
                    time.sleep(1)
                    print(nom2 + " ha quitado la última piedra, ", nom2 + " ha perdido.\nResetead el programa.")
                    sys.exit()
            
            if quitar < 1:
                print("Ese no es un número entre 1 y 3")
                correcto = True
            if 3 < quitar:
                print("Ese no es un número entre 1 y 3")
                correcto = True
        return (total)
    
    while jugando2:
        JUGADOR1()
        JUGADOR2()
