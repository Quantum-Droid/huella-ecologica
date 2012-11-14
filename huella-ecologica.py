# encoding: UTF-8
# Diegomf

# Programa de Cambio Climático

## LETS DO THIS SHIT!

########################################
# funcion mainMenu
# regresar lista con valores de t/f (8)
########################################



def menuPrincipal():
	
	print("¡Bienvenido a nuestro programa para calcular tu Huella Ecológica!")
	print("En este programa sabrás tu Huella Ecológica y la prodrás comparar con la de otras personas en el mundo")

	initialize = str(input("Teclea ENTER para empezar")) 
	
	f_questions = open("Questions", "r")
	questions = f_questions.readlines()
	f_questions.close()
	answers = []

	for line in questions:
		answers.append(exeQuestion(line))	
	
	number = process(answers)
	print("Tu Huella Ecológica es: %i " % (number))

def exeQuestions(question):
	notAccepted = False 
	while notAccepted:
		try:
			a = int(input(question))
		except ValueError:
			print("Valor no válido, intenta de nuevo")
		if a == 1 :
			return True
		elif a == 2:
			return False
		elif a == 999:
			print("Lol faggot!!")
			a
		else:
			print("Valor no válido, intenta de nuevo")

"Teclea 1 si consumes más productos animales que vegetales. Teclea 2 si consumes más productos vegetales que animales"
