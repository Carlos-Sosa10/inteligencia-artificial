
import json
import random
from operator import itemgetter

with open('subida.json') as file:
	data = json.load(file)

ruta=[]
camino=[]
otro = []
def subida(inicial,objetivo,ant):
    ruta.append(inicial)
    print("La ruta inicial es "+inicial)
    print("La ruta anterior fue "+ant)
    if otro:
        del otro[:]
        del camino[:]
    if objetivo == inicial:
        print("el valor ha sido encontrado")
        return inicial
    if ant == "":
        ant = inicial
    for d in data:
        if d[0] == inicial:
            if ant != "":
                if d[1] != ant:
                    camino.append(d)
    print(min(camino, key=itemgetter(2))[:])
    print (camino)
    chi = (min(camino, key=itemgetter(2))[2])
   
    for c in camino:
        if c[2] == chi:
            print("entra")
            otro.append(c)
    print("valores definitivos")
    print(otro)
    cont = 0
    for n in otro:
        cont = cont +1
        if cont > 1:
            r = random.random()
            print("n")
            print(n)
            if r < 0.5:
                otro.pop()
            else: 
                otro.pop(0)
        else:
            print(otro)
    if otro:
        for n in otro:
            print("nodo")
            print(n[1])
            return subida(n[1],objetivo,inicial)

                
arch=subida("Z","I","")
if arch:
    print("nodo")
    print(arch)
    print("ruta")
    print(ruta)
