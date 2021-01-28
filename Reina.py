matriz =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#guarda posicion 
posAct=[]
llave = 0

posiciones = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def entrada(nreinas, matriz, llave,posiciones):
    backup = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    cont = 0
    print("nreinas "+str(nreinas))
 
    if nreinas == 1:
        return solucion(matriz)
    else: 
        for t in range(len(matriz)):
            for r in range(len(matriz[t])):
                
                if cont == 0:
					
                    if posiciones[t][r] != 3:
                        if(matriz[t][r] == 0):

                            if nreinas == 4:
                                posiciones[t][r] = 3
                            matriz[t][r] = 1
                            cont = cont + 1
                            posAct.append([t,r])

        matriz = iterar(matriz,posAct)

        posAct.pop(0)
        for t in matriz:

            if 0 in t:
                llave = 0
            else:
                llave = 1
        if llave == 1:
            print(llave)
            for t in backup:
                print(t)
            nreinas=4
            llave=0
            return entrada(nreinas,backup,llave,posiciones)
        if llave == 0:
            print(llave)
            nreinas=nreinas-1
            return entrada(nreinas,matriz,llave,posiciones)
#Rev de diagonales verticales y horizontales
def iterar(matriz,posAct):
    print("#####################################################################")
    a = posAct[0][0]
    b = posAct[0][1]
    r = range(len(matriz))
    bb = b
    aa = a
    print(posAct)
    
    for t in range(len(matriz)):
        for r in range(len(matriz[t])):
            matriz[a][r] = 2
            matriz[t][b] = 2
    imp(matriz)
    for t in range(len(matriz)):
        bb = bb-1
        aa = aa -1
        if (bb >= 0)and(aa >=0):
            print("- -")
            matriz[aa][bb] = 2
    bb = b
    aa = a
    imp(matriz)
    for t in range(len(matriz)):
        aa = aa +1
        bb = bb +1
        if (aa <= r)and(bb <= r):
            print("+ +")
            matriz[aa][bb] = 2

    bb = b
    aa = a
    imp(matriz)
    for t in range(len(matriz)):
        bb = bb+1
        aa = aa -1
        if (bb < r)and(aa >=0):
            print("+ -")
            matriz[aa][bb] = 2
    bb = b
    aa = a
    imp(matriz)
    for t in range(len(matriz)):
        bb = bb-1
        aa = aa + 1
        if (bb >= 0)and(aa <r):
            print("- +")
            matriz[aa][bb] = 2
    matriz[a][b]=1
    imp(matriz)
    print("#####################################################################")
    return matriz
    
#caso especial
def solucion(matriz):
    for t in range(len(matriz)):
        for r in range(len(matriz[t])):
            if (matriz[t][r]) == 0:
                 matriz[t][r] = 1
    print("###########resultado#################")
    for t in matriz:
        print(t)

def imp(matriz):
    print("#####################################################################")
    for t in matriz:
        print(t)

entrada(4,matriz,0,posiciones)
