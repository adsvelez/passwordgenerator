import random

def generador(num,longitud):

    print("#############################")
    print("### Password Generator V1 ###")
    print("#############################")
    print("* Política actual: ")
    print("*** Número de passwords: " + str(num))
    print("*** Longitud de passwords: " + str(longitud))
    print("*** Contiene mayus, minus, numeros y simbolos: Si")
    print("#############################")

    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
    simbolos = "!#$%&/()=?*_:;-.,+@"
    numeros = "1234567890"
    minusculas = "abcdefghijklmnopqrstuvxyz"

    caracteres = mayusculas+simbolos+numeros+minusculas

    tiene_mayus = False
    tiene_simbolos = False
    tiene_numeros = False
    tiene_minusculas = False

    print("* Passwords generados: ")

    for i in range(num):
        password = ''
        cumple = False
        while cumple == False:
            for c in range(longitud):
                password += random.choice(caracteres)            
            
            for char in password:
                if char in mayusculas:
                    tiene_mayus = True
                elif char in simbolos:
                    tiene_simbolos = True
                elif char in numeros:
                    tiene_numeros = True
                elif char in minusculas:
                    tiene_minusculas = True
            if tiene_mayus and tiene_minusculas and tiene_numeros and tiene_simbolos:
                cumple = True
                print(password)
            else:              
                cumple = False
                tiene_mayus = False
                tiene_simbolos = False
                tiene_numeros = False
                tiene_minusculas = False
                password = ''
                
def policy():
    print("##############################")
    print("### Edición de la política ###")
    print("##############################")
    num = 0
    while  num < 1 or num > 100:
        num = int(input("Cuantos passwords desea generar? [1-100] "))

    longitud = 0
    while  longitud < 4 or longitud > 50:
        longitud = int(input("Cual es la longitud de los passwords [4-50]? "))
    
    generador(num,longitud)

def menu():
    num = 1
    longitud = 12
    print("#############################")
    print("### Password Generator V1 ###")
    print("#############################")
    print("* Política actual: ")
    print("*** Número de passwords: " + str(num))
    print("*** Longitud de passwords: " + str(longitud))
    print("*** Contiene mayus, minus, numeros y simbolos: Si")
    print("#############################")
    print("1. Generar passwords")
    print("2. Cambiar política de passwords")
    print("3. Salir")

    opcion=input(" Que opcion desea? ... ")

    while not opcion.isdigit() or opcion > "3" or opcion <= "0":
        print("Opción invalida, seleccione una opción del 1 al 3")
        opcion=input(" Que opcion desea? ... ")

    if opcion == "1":
        generador(num,longitud)
    if opcion == "2":
        policy()
    if opcion == "3":
        print ("Adios")

menu()