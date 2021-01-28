
import json
with open('profundidad.json') as file:
	data = json.load(file)
camino=[]

def busqueda(inicio,busq):
	
	if inicio == busq:
		return busq
		
	for j in data:
		if j[0] == inicio:
			camino.append(inicio)
			print(j[0])
			resultado=busqueda(j[1],busq)
			if resultado:
				return resultado
	camino.pop()
	
resultado=busqueda("C:","AccesoALaNasa.exe")
if resultado:
	print ("Archivo encontrado")
	print(camino)
else:
	print("no encontrado")
