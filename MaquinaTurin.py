entrada = input("Intruduce la cadena inicial: ") #cadena inicial que recibe
tamano = len(entrada)                            #tamaño de la cadena
cinta1 = []                                      #guarda la cadena inicial
cinta2 = []                                      #guarda los 1
cinta3 = []                                      #guarda los 0

#------ Start of funtions -------
def validator(cinta1, cinta2, cinta3, tamano):
    for i in range(0, tamano):
        if "1" in entrada[i]:                           #valida si hay un uno dentro de la cadena
            cinta2[len(cinta2):] = [entrada[i]]         #agrega el numero a la cinta
            print("cinta2" + str(cinta2))
        else:
            if "0" in entrada[i]:
                cinta3[len(cinta3):] = [entrada[i]]     #agrega el numero a la cinta
                print("Cinta3" + str(cinta3))           #str() sirve para imprimir Strings 

    print("----- Valores de las Cintas -------")
    print("Cinta 1: " + str(cinta1))
    print("Cinta 2: " + str(cinta2))
    print("Cinta 3: " + str(cinta3))


def validatorTam(cinta2, cinta3):
    while True: 
        if not cinta2 and cinta3:
            print("\nLa cinta 2 es menor que la cinta 3")
            break
        elif not cinta3 and cinta2:
            print("\nLa cinta 3 es menor que la cinta 2")
            break
        elif not cinta2 and not cinta3:
            print("\nLas cintas son del mismo tamaño")
            break
        else:
            cinta2.pop()                                    #libera la cinta 2
            cinta3.pop()                                    #libera la cinta 3
#------- End of funtions -----------

#---- Principal ---- 
if entrada.isdigit():                                       #valida que lo introducido sean digitos.
    cinta1.append(entrada)                                  #inserta la entrada en la cinta1.
    validator(cinta1, cinta2, cinta3, tamano)               #Llama a la función para separar digitos.
    validatorTam(cinta2, cinta3)                            #Llama a la función para validar tamaños.
else:
    print("Ingrese valores numericos")

