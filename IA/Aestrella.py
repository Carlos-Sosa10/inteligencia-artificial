# Sosa Rodriguez Carlos Eduardo
import queue

def Lab():
	lab = [["||","||", "||", "||", "||", "O", "||", "||", "||"],
	["||"," ", " ", " ", " ", " ", " ", " ", "||"],
	["||"," ", "||", "||", " ", "||", "||", " ", "||"],
	["||"," ", "||", " ", " ", " ", "||", " ", "||"],
	["||"," ", "||", "X", "||", " ", "||", " ", "||"],
	["||"," ", "||", " ", "||", " ", "||", " ", "||"],
	["||"," ", "||", " ", "||", " ", "||", "||", "||"],
	["||"," ", " ", " ", " ", " ", " ", " ", "||"],
	["||","||", "||", "||", "||", "||", "||", "||", "||"]]

	return lab


def printlab(lab, path=""):
	for x, posicion in enumerate(lab[0]):
		if posicion == "O":
			start = x

	i = start
	j = 0
	posicion = set()
	for mov in path:
		if mov == "L":
			i -= 1

		elif mov == "R":
			i += 1

		elif mov == "U":
			j -= 1

		elif mov == "D":
			j += 1
		posicion.add((j, i))

	for j, row in enumerate(lab):
		for i, col in enumerate(row):
			if (j, i) in posicion:
				print("+ ", end="")
			else:
				print(col + " ", end="")
		print()



def valid(lab, movimientos):
	for x, posicion in enumerate(lab[0]):
		if posicion == "O":
			start = x

	i = start
	j = 0
	for mov in movimientos:
		if mov == "L":
			i -= 1

		elif mov == "R":
			i += 1

		elif mov == "U":
			j -= 1

		elif mov == "D":
			j += 1

		if not(0 <= i < len(lab[0]) and 0 <= j < len(lab)):
			return False
		elif (lab[j][i] == "||"):
			return False

	return True


def findEnd(lab, movimientos):
	for x, posicion in enumerate(lab[0]):
		if posicion == "O":
			start = x

	i = start
	j = 0
	for mov in movimientos:
		if mov == "L":
			i -= 1

		elif mov == "R":
			i += 1

		elif mov == "U":
			j -= 1

		elif mov == "D":
			j += 1

	if lab[j][i] == "X":
		print("Encontrado: " + movimientos)
		printlab(lab, movimientos)
		return True

	return False




x = queue.Queue()
x.put("")
add = ""
lab  = Lab()

while not findEnd(lab, add): 
	add = x.get()
	#print(add)
	for j in ["L", "R", "U", "D"]:
		put = add + j
		if valid(lab, put):
			x.put(put)
