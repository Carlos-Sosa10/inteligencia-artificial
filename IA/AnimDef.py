import json
ave=0
reptil=0
mamifero=0
with open('animales.json') as fichero:
	data = json.load(fichero)
nombre=input("Nombre de tu animal:")
for e in data['defecto']:
	if nombre == e['nombre']:
		print('MAMIFERO')
		
		exit()

for pregunta in data['Nodo']:
	print('¿Tiene o puede?')
	print(pregunta[1])
	R=input("")
	if R == "si":
		ave=ave+pregunta[2]['Ave']
		reptil=reptil+pregunta[2]['Reptil']
		mamifero=mamifero+pregunta[2]['Mamifero']
print('AVE:' + str(ave))
p1=(ave/(ave+reptil+mamifero))*100
print('Porcentaje ave:'+str(p1))
print('REPTIL:' + str(reptil))
p2=(reptil/(ave+reptil+mamifero))*100
print('Porcentaje reptil:'+str(p2))
print('MAMIFERO:' + str(mamifero))
p3=(mamifero/(ave+reptil+mamifero))*100
print('Porcentaje mamifero:'+str(p3))
if ave > reptil and ave > mamifero:
	print('Tu animal es una ave')
	print('Con un valor de =>' + str(ave))
if reptil > ave and reptil > mamifero:
	print('Tu animal es una reptil')
	print('Con un valor de =>' + str(reptil))
if mamifero > ave and mamifero > reptil:
	print('Tu animal es una mamifero')
	print('Con un valor de =>' + str(mamifero))

