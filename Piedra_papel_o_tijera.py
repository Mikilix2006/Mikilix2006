import random
import sys
import time

opciones = {1:"piedra", 
            2:"papel", 
            3:"tijera"
            }

vidasjug = 3
vidasia = 3
jugando = True
    
def ia():
    global iaseleccion
    iaseleccion = random.randint(1,3)
    iaseleccion = opciones[iaseleccion]
    return iaseleccion

def jugador():
    global jugseleccion
    jugseleccion = int(input("Elige tu jugada. 1:Piedra, 2:Papel, 3:Tijera:  "))
    jugseleccion = opciones[jugseleccion]
    return jugseleccion

def fin():
    global jugando
    #Si alguno se ha quedado sin vidas
    if vidasia == 0:
        print("La IA se ha quedado sin vidas, has ganado.")
        jugando = False
        sys.exit()
    
    if vidasjug == 0:
        print("Te has quedado sin vidas, has perdido.")
        jugando = False
        sys.exit()

def jugpierde():
    global vidasjug
    print("Has perdido una vida, la IA ha elegido ",iaseleccion, ".")
    vidasjug = vidasjug - 1
    time.sleep(1)
    print("Te quedan ", vidasjug, " vidas.")
    fin()
    
def iapierde():
    global vidasia
    print(jugseleccion, " gana a ",iaseleccion, "la IA pierde una vida.")
    vidasia = vidasia - 1
    time.sleep(1)
    print("A la IA le quedan ", vidasia, " vidas.")
    fin()
    
def empate():
    print("Empate, nadie pierde vidas.")
    time.sleep(1)

def comprobacion():
    global vidasia
    global vidasjug
            
    #Si la IA elige piedra
    if iaseleccion == opciones[1]:
        
        #Si el jugador elige piedra
        if jugseleccion == opciones[1]:
            empate()

        #Si el jugador elige papel
        if jugseleccion == opciones[2]:
            iapierde()
            
        #Si el jugador elige tijeras
        if jugseleccion == opciones[3]:
            jugpierde()
            
    #Si la IA elige papel
    if iaseleccion == opciones[2]:
        
        #Si el jugador elige papel
        if jugseleccion == opciones[2]:
            empate()

        #Si el jugador elige tijeras
        if jugseleccion == opciones[3]:
            iapierde()
            
        #Si el jugador elige piedra
        if jugseleccion == opciones[1]:
            jugpierde()
            
    #Si la IA elige tijeras
    if iaseleccion == opciones[3]:
        
        #Si el jugador elige tijeras
        if jugseleccion == opciones[3]:
            empate()

        #Si el jugador elige piedra
        if jugseleccion == opciones[1]:
            iapierde()
            
        #Si el jugador elige papel
        if jugseleccion == opciones[2]:
            jugpierde()
        
#Comienza el juego
while jugando == True:
    ia()
    jugador()
    comprobacion()
