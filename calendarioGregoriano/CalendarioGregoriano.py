"""
R0:
"""
def fecha_es_tupla(paramFecha):
    if isinstance(paramFecha, tuple):
        if len(paramFecha) == 3:
            for item in paramFecha:
                if not isinstance(item, int) or item < 0:
                    print("La tupla introducida contiene items no numerales o menores a 0")
                    return False
            return True
        else:
            print("La cantidad de items en la tupla es diferente de 3 \n")
            return False
    else:
        print("El parámetro introducido no es una tupla \n")
        return False


"""
R1: dado un año dentro del rango definido (rango) determinar si el año es o 
no bisiesto
Input: entero númerico
Output: Boolean 
"""
def bisiesto(anno):
    if anno % 4 != 0:  # no es múltiplo de 4, no es bisiesto
        return False
    else:  # es múltiplo de 4
        if anno % 100 == 0:  # es múltiplo de 100
            if anno % 400 == 0:  # es múltiplo de 400
                return True  # es bisiesto porque cumple con las tres condiciones
            else:
                return False  # no es bisiesto porque no es múltiplo de 400
        else:  # no es múltiplo de 100 ni de 400
            return True


"""
    R2: Verifica si una fecha es válida en el Calendario Gregoriano
"""
def fecha_es_valida(tupla):
    if fecha_es_tupla(tupla):
        if (tupla[0] == 1582):
            if tupla[1] >= 10 and tupla[2] >= 15 and tupla[2] <= 31:
                return True
            else:
                print("La fecha ingresada no es válida en el Calendario Gregoriano para el año 1582\n")
                return False
        elif tupla[0] > 1582:
            if dia_es_valido(tupla):
                return True
            else:
                print("La fecha ingresada no es válida en el Calendario Gregoriano.\n")
                return False
        else:
            print('El año ingresado no es válido en el Calendario Gregoriano\n')
            return False
    else:
        print("La fecha debe ser ingresada como una tupla de enteros con formato (año, mes, día)")
        return False

"""
R3: dada una fecha válida, determinar la fecha del día siguiente
Input: tupla de fecha
Output: tupla de una fecha válida
"""
def dia_siguiente(tupla):
    anno = tupla[0]
    mes = tupla[1]
    dia = tupla[2]
    meses30dias = [2, 4, 6, 9, 11]
    if fecha_es_valida(tupla):
        if dia < 28:
            return anno, mes, dia + 1
        else:  # para los días 29, 30 y 31
            if mes in meses30dias:
                if mes != 2:
                    if dia < 30:  # para los días 28 y 29
                        return anno, mes, dia + 1
                    else:
                        return anno, mes + 1, 1
                else:
                    if bisiesto(anno) and dia == 28:
                        return anno, 2, 29
                    else:
                        return anno, 3, 1
            else:
                if dia == 31:
                    if mes == 12:
                        return anno + 1, 1, 1
                    else:
                        return anno, mes + 1, 1
                else:
                    if dia < 31:  # para los días 28, 29 y 30
                        return anno, mes, dia + 1
    else:
        return ()

"""
    R4: determina cuál es la posición de la fecha dada dentro del año dado
    Retorna un entero con el valor de la posición
"""
def ordinal_dia(tupla):
    ordinal = 1

    if fecha_es_valida(tupla):
        if (tupla[0] == 1582):
            fecha_base = (tupla[0], 10, 15)
        else:
            fecha_base = (tupla[0], 1, 1)   
        proximo_dia = dia_siguiente(fecha_base)

        if(fecha_base != tupla):
            while(proximo_dia != tupla):
                ordinal += 1
                proximo_dia = dia_siguiente(proximo_dia)
            ordinal += 1

            print("La posición de la fecha ingresada en el año es: " , ordinal, "\n")
            return ordinal
        else:
            print("La posición de la fecha ingresada en el año es: " , ordinal, "\n")
            return ordinal
    else:
        print("La fecha ingresada no es válida \n")
        return 0

"""
    Verifica si el día ingresado es válido según el mes ingresado 
    y si el año es bisiesto o no.
"""
def dia_es_valido(tupla):
    mes31 = [1, 3, 5, 7, 8, 10, 12]  # meses que tienen 31 días
    mes30 = [4, 6, 9, 11]  # meses que tienen 30 días
    mesbisiesto = [2]  # meses que pueden ser bisiesto

    if tupla[1] in mesbisiesto:
        if bisiesto(tupla[0]) and tupla[2] >= 1 and tupla[2] <= 29:
            return True
        elif not bisiesto(tupla[0]) and tupla[2] >= 1 and tupla[2] <= 28:
            return True
        else:
            return False
    elif tupla[1] in mes31 and tupla[2] >= 1 and tupla[2] <= 31:
        return True
    elif tupla[1] in mes30 and tupla[2] >= 1 and tupla[2] <= 30:
        return True
    else:
        return False


 ## Formula de Zeller para calcular dia de una fecha especifica
def diaFecha(tupla):
    dia = tupla[2]
    mes = tupla[1]
    anno = tupla[0]
    if mes < 3:
        mes = mes + 12
        anno = anno - 1
    dia = (((13 * mes + 3) // 5 + dia + anno + (anno / 4) - (anno // 100) + (anno // 400)) % 7)
    return int(dia)*4 + 4


"""
    R5: Imprime en 3 lineas de 4 meses el calendario anual de la fecha proporcionada
"""
def imprimir_3x4(tupla):

    anno = tupla[0]
    mesActual = 1
    diaActual = 1               #variables de medicion
    nuevaTupla = (anno,1,1)
    x = 1
    espaciosInicio = ""
    cantEspacios = diaFecha(nuevaTupla)
    lineDicc = { 1:[] , 2:[],3:[],4:[]}   #diccionario de impresion

    while mesActual <= 12:      #avanza mes a mes

        lineaActual = "       "
        mesStr = str(mesActual)
        if mesActual < 10:
            mesStr = "0" + mesStr
        lineDicc[mesActual].append(lineaActual + mesStr + ")  L   K   M   J   V   S   D") #Header de cada mes

        if cantEspacios > 28:
            cantEspacios = 4
        for x in range(cantEspacios):      #Calculo del espacio para dia de la semana de inicio de mes
            espaciosInicio += " "

        lineaActual += espaciosInicio + "01"
        espaciosInicio = ""
        diaActual += 1

        while diaActual > 1:        #avanza dia a dia en un mes
            cantEspacios += 4
            if cantEspacios > 28:   #Si ya llego a domingo pasar a linea siguiente (Lunes)
                lineDicc[mesActual].append(lineaActual)
                lineaActual = "         "
                cantEspacios = 4
            strDia = str(diaActual)
            if diaActual < 10:
                strDia = "0" + strDia
            lineaActual += "  " + strDia  # A la linea actual en el mes se le suma el nuevo dia
            diaActual = (dia_siguiente((anno, mesActual, diaActual)))[2]    #Se pasa de dia


        lineDicc[mesActual].append(lineaActual) #Se llena la ultima lidea del mes
        cantEspacios += 4
        mesActual += 1

        if mesActual == 5 or mesActual == 9 or mesActual == 13:  #Cada 4 meses se imprimen las lineas en orden de cada mes
            dicCounter = 0                                       #(Todas las primeras, todas las segundas...)
            while dicCounter <= 7:
                for key in lineDicc:
                    try:
                        print(lineDicc[key][dicCounter], end='')
                        longlin = 37 - len(lineDicc[key][dicCounter])
                        while longlin > 0:
                            print(" ", end='')                           #Para mantener el formato se imprimen siempre 7 lineas de 7 dias, si el orden no da para 7 lineas
                            longlin -= 1                                 #se rellena el espacio con " "
                    except:
                        print("                                     ", end='')

                        continue
                print("\n")
                dicCounter +=1
            if mesActual == 5:
                lineDicc = {5: [], 6: [], 7: [], 8: []}
            elif mesActual == 9:
                lineDicc = {9: [], 10: [], 11: [], 12: []}



def pedirFechaAux():
    anno = int(input("Ingrese un año: "))
    mes = int(input("Ingrese un mes: "))
    dia = int(input("Ingrese un día: "))
    return anno, mes, dia

def mainMenu():
    while (True):

        print(
            "\n 0  fecha_es_tupla\n 1  bisiesto\n 2  fecha_es_valida\n 3  dia_siguiente\n 4  ordinal_dia\n 5  imprimir_3x4\n 6  salir\n")
        try:
            numChoice = int(input("Digite el número de la opción que desea ejecutar: "))

            if numChoice == 0:
                print("\nIntroduzca los tres valores de la fecha para verificar que sean números enteros")
                print("\nLa fecha es tupla: ", fecha_es_tupla(pedirFechaAux()))
                input()
            elif numChoice == 1:
                anno = int(input("\nIngrese un año para verificar que sea bisiesto: "))
                print("\nEl año es bisiesto: ", bisiesto(anno))
                input()
            elif numChoice == 2:
                print("Ingrese una fecha para verificar que sea válida según el calendario gregoriano")
                print("\nLa fecha es válida: ", fecha_es_valida(pedirFechaAux()))
                input()
            elif numChoice == 3:
                print("Ingrese una fecha para determinar la fecha del día siguiente")
                print("\nLa fecha siguiente es: ", dia_siguiente(pedirFechaAux()))
                input()
            elif numChoice == 4:
                print("Ingrese una fecha para determinar el ordinal")
                ordinal_dia(pedirFechaAux())
                input()
            elif numChoice == 5:
                print("Ingrese una fecha para imprimir el calendario gregoriano de su año")
                imprimir_3x4(pedirFechaAux())
                input()
            elif numChoice == 6:
                return
            else:
                print("Número inválido")

        except:
            print("Caracter Inválido")
        print("***********************************************************************************************")

mainMenu()

#tupla = (2001,15,7)
# fecha_es_tupla(tupla)

# print(bisiesto(2035))
# print(dia_siguiente((2020, 2, 15)))

# pruebas = [(2022, 1, 3), (2020, 2, 29), (2020, 2, 16), (2020, 2, 28), (2027, 3, 7), (2092, 4, 30), (2098, 5, 31), (2434, 6, 5), (2022, 7, 18), (2020, 8, 30), (2021, 9, 27), (2028, 10, 29), (2014, 11, 30), (2015, 12, 4), (2032, 12, 31)]
#pruebas = [1992, 2016, 1582, 2017, 2020, 3542, 1852, 2012]
#print("Pruebas R1")
#for anno in pruebas:
# print("Año: ", anno, " Es bisiesto: ", bisiesto(anno))
    # print("\n")

#imprimir_3x4(tupla)

