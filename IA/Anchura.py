

import json
with open('Anchura.json') as file:
	data = json.load(file)
concluidos =[]
guia=[]
otro = []
siguienteNodo=[]

def priAnchura(Carpeta,Archivo):
	
	if Carpeta == Archivo:
		return Archivo
	if siguienteNodo:
		contador = 0
		for X in siguienteNodo:
			 contador += 1
		if contador > 1:
			print("Nodo principal: " +siguienteNodo[0])
			siguienteNodo.pop(0)
	if otro:
		del otro[:]
	for i in data:
		if i[0] == Carpeta:
			siguienteNodo.append(i[1])
			otro.append(i[0])
			if i[1] == Archivo:
				nodo = priAnchura(i[1],Archivo)
				return nodo
	concluidos.append(list(set(otro)))
	if concluidos:
		print("Nodos Recorridos Adyacentemente")
		print(str(concluidos))
		print(siguienteNodo[0])
		guia.append(siguienteNodo[0])
		return priAnchura(siguienteNodo[0],Archivo)

nodo = priAnchura("C:","Me Reprobaron.jpg")
print("Hijo encontrado en el nodo principal: " +nodo)
cam = []
if nodo:
	for c in guia:
		if c not in cam:
			cam.append(c)
	print("Padres(Nodos Revisados)")
	print(cam)
else:
	print("No se encontro")


