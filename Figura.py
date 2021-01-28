preguntas = [
["FG","A"],
["FG","B"],
["FG","C"],
["Triangulo","BA"],
["Triangulo","BB"],
["Triangulo","BC"],
["Triangulo","BD"]

],
Respuestas = [
['B','Triangulo'],
['BA','Triangulo recto'],
['BB','Triangulo Equilatero'],
['BC','Triangulo Isosceles'],
['BD','Triangulo Escaleno'],
]

Textos = {
"FG":'Cuantos Lados Tiene',
"A"='4 Lados',
"B":'Tres Lados',
"C":'Ningun Lado',
"BA":'Tiene un Lado recto',
"BB":'Tiene Todos sus Lados iguales',
"BC":'Dos Lados iguales',
"BD":'Todos Diferentes',
"Triangulo":'Caracteristica de Tu Triangulo',
}
}

Inicial="FG"
####################
Estado=Inicial
print(Textos[Estado])
opc= [e[1] for e in Preguntas if e[0]==Estado ]
for on in opc:
print(o+ " "+Textos[o])
R= input(" ")
Sig=[e[1] for e in Respuestas if e[0] ==R][0]
Estado=(sig)
