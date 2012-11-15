#!/usr/bin/python3
# encoding: UTF-8
# Sauλ de Nova and Diegomf

def mainMenu():
	"""
	Interface that interacts with the user and asks him for his data.
	"""
	print("¡Bienvenido a nuestro programa para calcular tu Huella Ecológica!")
	print("En este programa sabrás tu Huella Ecológica y la podrás comparar con la de otras personas en el mundo")

	initialize = str(input("Teclea ENTER para empezar")) 
	
	f_questions = open("Questions.txt", "r")
	questions = f_questions.readlines()
	f_questions.close()
	answers = []

	for line in questions:
		answers.append(exeQuestions(line))	
	
	value = process(answers)
	print("Tu Huella Ecológica es: %i " % (value))

def exeQuestions(question, valueTrue=1, valueFalse=2):
	"""
	Generic template for obtaining results from the user, 
	Gets from the user either a valueTrue, valueFalse
	Returns a boolean, 1->True, 2->False
	"""
	accepted = False
	while not accepted:
		try:
			a = int(input(question))
		except ValueError:
			print("Valor no válido, intenta de nuevo")
			continue
		if a == valueTrue or a == valueFalse:
			returnVal = True
			if a == valueFalse: # If a is equal to false, then returnVal is false, else true
				returnVal = False
			accepted = True
		elif a == 999: # Easter egg
			print("Lol faggot!!")
		else:
			print("Valor no válido, intenta de nuevo")
	return returnVal

def process(dataList):
	"""
	Receives the list of the values obtained from the questions and from the
	value of the valoresHuella.txt file and calculates the result of the exam
	returns the sum of the values
	"""
	archivoValores = open("valoresHuella.txt", "r")
	sumValues = sum([int(archivoValores.readline().split(" ")[0 if dataList[i] else 1]) for i in range(len(dataList))])
	archivoValores.close()
	return sumValues 

if __name__ == "__main__":
	mainMenu()

