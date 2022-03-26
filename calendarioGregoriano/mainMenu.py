#from R0_fecha_es_tupla import fecha_es_tupla


def mainMenu(fechaIntroducida):

    while(True):

        print("\n 0  fecha_es_tupla\n 1  bisiesto\n 2  fecha_es_valida\n 3  dia_siguiente\n 4  ordinal_dia\n 5  imprimir_3x4\n 6  salir\n")

        try:
            numChoice = int(input("Digite el número de la opción que desea ejecutar: "))

            if numChoice == 0:
               #print(fecha_es_tupla(fechaIntroducida));
                print()
            elif numChoice == 1:
                print(1)
            elif numChoice == 2:
                print(2)
            elif numChoice == 3:
                print(3)
            elif numChoice == 4:
                print(4)
            elif numChoice == 5:
                print(5)
            elif numChoice == 6:
                return
            else:
                print("Número inválido")

        except:
            print("Caracter Inválido")



tupla = (5,6,-1)
mainMenu(tupla)
