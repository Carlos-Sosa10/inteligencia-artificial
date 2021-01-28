import json

with open('BasedeConocimiento.json') as file:
	data = json.load(file)

inicial = 'FG'
i = data['Textos']
print(i[inicial])
Estado = inicial
print(i['FG'])
opc = [e[1] for e in data['Preguntas'] if e[0]==Estado]
for o in opc:
	print(o+" "+data['Textos'][o])
R = input("")
Sig = [e[1] for e in data['Respuestas'] if e[0] == R][0]
Estado = Sig
print(Estado)

def funcionPreguntar(Estado):
		inicial = Estado
		i = data['Textos']
		print(i[inicial])
		Estado=inicial
		print(i[Estado])
		op = [e[1] for e in data['Preguntas'] if e[0]==Estado]
		for o in op:
			print(o+" "+data['Textos'][o])
		R = input("")
		sig = [e[1] for e in data['Respuestas'] if e[0] ==R][0]
		Estado = sig
		print (Estado)
if Estado == 'Cuadrilatero':
	funcionPreguntar(Estado)
if Estado == 'Triangulo':
	funcionPreguntar(Estado)
if Estado == 'Figura Conica':
	funcionPreguntar(Estado)

