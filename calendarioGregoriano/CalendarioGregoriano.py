from datetime import date

# Funciones principales
"""
    R0: verifica que el dato ingresados esa una tupla de tres valores positivos
    Input: tupla
    Output: Boolean
"""
def fecha_es_tupla(paramFecha):
    if isinstance(paramFecha, tuple):
        if len(paramFecha) == 3:
            for item in paramFecha:
                if not isinstance(item, int) or item < 0:
                    #print("La tupla introducida contiene items no numerales o menores a 0")
                    return False
            return True
        else:
            #print("La cantidad de items en la tupla es diferente de 3 \n")
            return False
    else:
        #print("El parámetro introducido no es una tupla \n")
        return False

"""
    R1: dado un año dentro del rango definido determinar si el año es o 
    no bisiesto
    Input: entero númerico
    Output: Boolean 
"""
def bisiesto(anno):
    if anno >= 1582:
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
    else:
        return False

"""
    R2: Verifica si una fecha es válida en el Calendario Gregoriano
    Input: Tupla
    Output: Boolean
"""
def fecha_es_valida(tupla):
    if fecha_es_tupla(tupla):
        if (tupla[0] == 1582):
            if tupla[1] >= 10 and tupla[2] >= 15 and tupla[2] <= 31:
                return True
            else:
                #print("La fecha ingresada no es válida en el Calendario Gregoriano para el año 1582\n")
                return False
        elif tupla[0] > 1582:
            if dia_es_valido(tupla):
                return True
            else:
                #print("La fecha ingresada no es válida en el Calendario Gregoriano.\n")
                return False
        else:
            #print('El año ingresado no es válido en el Calendario Gregoriano\n')
            return False
    else:
        #print("La fecha debe ser ingresada como una tupla de enteros con formato (año, mes, día)")
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
    Input: tupla
    Output: Boolean
"""
def ordinal_dia(tupla):
    ordinal = 1

    if fecha_es_valida(tupla):
        if (tupla[0] == 1582):
            return 0
        else:
            fecha_base = (tupla[0], 1, 1)
        proximo_dia = dia_siguiente(fecha_base)

        if (fecha_base != tupla):
            while (proximo_dia != tupla):
                ordinal += 1
                proximo_dia = dia_siguiente(proximo_dia)
            ordinal += 1

            return ordinal
        else:
            return ordinal
    else:
        print("La fecha ingresada no es válida \n")
        return 0

"""
    R5: Imprime en 3 lineas de 4 meses el calendario anual de la fecha proporcionada
    Input: valor númerico del año
"""
def imprimir_3x4(annoParam):
    anno = annoParam
    mesActual = 1
    diaActual = 1  # variables de medicion
    nuevaTupla = (anno, 1, 1)
    x = 1
    espaciosInicio = ""
    cantEspacios = diaFecha(nuevaTupla)
    lineDicc = {1: [], 2: [], 3: [], 4: []}  # diccionario de impresion

    while mesActual <= 12:  # avanza mes a mes

        lineaActual = "       "
        mesStr = str(mesActual)
        if mesActual < 10:
            mesStr = "0" + mesStr
        lineDicc[mesActual].append(lineaActual + mesStr + ")  L   K   M   J   V   S   D")  # Header de cada mes

        if cantEspacios > 28:
            cantEspacios = 4
        for x in range(cantEspacios):  # Calculo del espacio para dia de la semana de inicio de mes
            espaciosInicio += " "

        lineaActual += espaciosInicio + "01"
        espaciosInicio = ""
        diaActual += 1

        while diaActual > 1:  # avanza dia a dia en un mes
            cantEspacios += 4
            if cantEspacios > 28:  # Si ya llego a domingo pasar a linea siguiente (Lunes)
                lineDicc[mesActual].append(lineaActual)
                lineaActual = "         "
                cantEspacios = 4
            strDia = str(diaActual)
            if diaActual < 10:
                strDia = "0" + strDia
            lineaActual += "  " + strDia  # A la linea actual en el mes se le suma el nuevo dia
            diaActual = (dia_siguiente((anno, mesActual, diaActual)))[2]  # Se pasa de dia

        lineDicc[mesActual].append(lineaActual)  # Se llena la ultima lidea del mes
        cantEspacios += 4
        mesActual += 1

        if mesActual == 5 or mesActual == 9 or mesActual == 13:  # Cada 4 meses se imprimen las lineas en orden de cada mes
            dicCounter = 0  # (Todas las primeras, todas las segundas...)
            while dicCounter <= 7:
                for key in lineDicc:
                    try:
                        print(lineDicc[key][dicCounter], end='')
                        longlin = 37 - len(lineDicc[key][dicCounter])
                        while longlin > 0:
                            print(" ",
                                  end='')  # Para mantener el formato se imprimen siempre 7 lineas de 7 dias, si el orden no da para 7 lineas
                            longlin -= 1  # se rellena el espacio con " "
                    except:
                        print("                                     ", end='')

                        continue
                print("\n")
                dicCounter += 1
            if mesActual == 5:
                lineDicc = {5: [], 6: [], 7: [], 8: []}
            elif mesActual == 9:
                lineDicc = {9: [], 10: [], 11: [], 12: []}

""" 
    R6: Auxiliar de diaFecha que devuelve un código dependiente del dia de la semana de la fecha proporcionada
    Codigo:  0 = domingo, 1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes, 6 = sábado
"""
def dia_semana (fecha):
    if(fecha_es_valida(fecha)):
        codigoDia = (diaFecha(fecha) - 4) / 4
        codigoDia = codigoDia + 1

        if codigoDia > 6:
            codigoDia = 0

        print("\n")
        return int(codigoDia)

""" 
    R7: determina la fecha que está n días naturales en el futuro
    Input: tupla fecha de inicio, int cantidad de días en el futuro
    Output: tupla con fecha válida
"""
def fecha_futura(fecha, diasFuturo):
    if fecha_es_valida(fecha):
        if diasFuturo == 0:
            return fecha
        elif diasFuturo > 0:
            n = 0
            fechaFuturo = fecha
            while diasFuturo > n:
                fechaFuturo = dia_siguiente(fechaFuturo)
                n += 1
            return fechaFuturo
        else:
            print("El número de días tiene que ser mayor o igual a 0")
            return ()
    else:
        return ()

""" 
    R8: determina la cantidad de dias pasados entre las dos fechas proporcionadas
    Input: tuplas con fechas válidad
    Output: int con la cantidad de días
"""
def dias_entre (fecha1, fecha2):
    if fecha_es_valida(fecha1) and fecha_es_valida(fecha2):

        fechaMayor = True

        if fecha1 == fecha2:
                return 0

        if fecha1[0] < fecha2[0]:
            fechaMayor = False
        elif fecha1[0] == fecha2[0]:

            if fecha1[1] < fecha2[1]:
                fechaMayor = False
            elif fecha1[1] == fecha2[1]:

                if fecha1[2] > fecha2[2]:
                    return fecha1[2] - fecha2[2]
                else:
                    return fecha2[2] - fecha1[2]

        contadorDias = 0
        if fechaMayor:
            tuplaAux = fecha2
            fecha2 = fecha1
            fecha1 = tuplaAux

        while fecha1 != fecha2:
            fecha1 = dia_siguiente(fecha1)
            contadorDias += 1

        print("\n")
        return contadorDias

"""
    R9: dadas dos fechas válidas (una de nacimiento y otra mayor)
        se determina la edad de la persona en años, meses y días
    Input: tuplas de fechas válidas
    Output: tupla de edad en años, meses y días
"""
def edad_al(tuplaFecha1, tuplaFecha2):
    if fecha_es_valida(tuplaFecha1) and fecha_es_valida(tuplaFecha2):
        if tuplaFecha1 <= tuplaFecha2:
            annos = calcular_anno(tuplaFecha1, tuplaFecha2)
            meses = calcular_meses(tuplaFecha1, tuplaFecha2)
            dias = calcular_dias(tuplaFecha1, tuplaFecha2)

            return (annos, meses, dias)
        else:
            return "La fecha 1 debe ser menor a la fecha 2"
    else:
        return "Alguna de las fechas ingresadas no es válida"

"""
    R10: obtiene la fecha del sistema en formato años, meses, dias
    Output: tupla con la fecha actual
"""
def fecha_hoy():
    fechaActual = str(date.today()).split("-")
    return (int(fechaActual[0]), int(fechaActual[1]), int(fechaActual[2]))

"""
    R11: permite calcular la edad en años, meses, días al día actual
         dada una fecha de nacimiento
    Input: tupla fecha de nacimiento
    Output: tupla edad en años, meses, dias
"""
def edad_hoy(tupla):
    if fecha_es_valida(tupla):
        fechaHoy = fecha_hoy()
        resultado = edad_al(tupla, fechaHoy)

        return resultado
    else:
        print("Alguna de las fechas ingresadas no es válida\n")
        return 0

# Funciones auxiliares
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
    return int(dia) * 4 + 4

def pedirFechaAux():
    anno = int(input("Ingrese un año: "))
    mes = int(input("Ingrese un mes: "))
    dia = int(input("Ingrese un día: "))
    return anno, mes, dia

"""
    Permite determinar la cantidad de días que tiene un mes
"""
def cantidad_dias(tupla):
    mes31 = [1, 3, 5, 7, 8, 10, 12]  # meses que tienen 31 días
    mes30 = [4, 6, 9, 11]            # meses que tienen 30 días
    mesbisiesto = [2]                # meses que pueden ser bisiesto

    if tupla[1] in mesbisiesto and bisiesto(tupla[0]) == False:
        return 28
    elif tupla[1] in mesbisiesto and bisiesto(tupla[0]):
        return 29
    elif tupla[1] in mes30:
        return 30
    else:
        return 31

"""
    Permite calcular la cantidad de años transcurridos entre una fecha y otra
"""
def calcular_anno(t1, t2):
    anno = t2[0] - t1[0]
    if t1[1] > t2[1]:
        anno -= 1
    if t1[1] == t2[1]:
        if t1[2] > t2[2]:        
            anno -= 1
    return anno

"""
    Permite calcular la cantidad dde meses que han pasado entre dos fechas
"""
def calcular_meses(t1, t2):
    meses = 0

    if t1[1] > t2[1]:
        meses = (12 - t1[1]) + t2[1]
    elif t1[1] < t2[1]:
        meses = t2[1] - t1[1]
    else:                               # mismo mes
        if t1[2] > t2[2]:
            meses = (12 - t1[1]) + t2[1]
        else:
            meses = 0
    
    # si en el último mes no ha pasado el día que se indica se debe restar 1
    if t1[2] > t2[2]:
        meses -= 1

    return meses

"""
    Permite calcular la cantidad de dias cumplidos de la persona
"""
def calcular_dias(t1, t2):
    dias = 0

    if t1[2] < t2[2]:
        dias = t2[2] - t1[2]
    elif t1[2] > t2[2]:
        mesAux = t2[1] - 1
        if mesAux == 0:
            mesAux = 12
        cantDias = cantidad_dias((t1[0], mesAux, t1[2]))
        dias = (cantDias - t1[2]) + t2[2]
    else:
        dias = 0

    return dias


def mainMenu():
    while (True):

        print("\n 0  fecha_es_tupla\n 1  bisiesto\n 2  fecha_es_valida\n 3  dia_siguiente\n 4  ordinal_dia\n 5  "
              "imprimir_3x4\n 6  dia_semana\n 7  fecha_futura\n 8  dias_entre\n 9  edad_al\n10  fecha_hoy\n11  edad_hoy\n12  salir\n")
        try:
            numChoice = int(input("Digite el número de la opción que desea ejecutar: "))

            if numChoice == 0:
                print("\nIntroduzca los tres valores de la fecha para verificar que sean números enteros")
                print("\nLa fecha es tupla: ", fecha_es_tupla(pedirFechaAux()))
                print("\n")
            elif numChoice == 1:
                anno = int(input("\nIngrese un año para verificar que sea bisiesto: "))
                print("\nEl año es bisiesto: ", bisiesto(anno))
                print("\n")
            elif numChoice == 2:
                print("\nIngrese una fecha para verificar que sea válida según el calendario gregoriano")
                print("\nLa fecha es válida: ", fecha_es_valida(pedirFechaAux()))
                print("\n")
            elif numChoice == 3:
                print("\nIngrese una fecha para determinar la fecha del día siguiente")
                print("\nLa fecha siguiente es: ", dia_siguiente(pedirFechaAux()))
                print("\n")
            elif numChoice == 4:
                print("\nIngrese una fecha para determinar el ordinal")
                ordinal = ordinal_dia(pedirFechaAux())
                if ordinal == 0:
                    print("\nNo se puede calcular el ordinal de la fecha ingresada")
                else:
                    print("\nEl ordinal de la fecha ingresada es: ", ordinal)
                print("\n")
            elif numChoice == 5:
                anno = int(input("\nIngrese un año para imprimir su calendario gregoriano: "))
                imprimir_3x4(anno)
                print("\n")
            elif numChoice == 5:
                anno = int(input("\nIngrese un año para imprimir su calendario gregoriano: "))
                imprimir_3x4(anno)
                print("\n")
            elif numChoice == 5:
                anno = int(input("\nIngrese un año para imprimir su calendario gregoriano: "))
                imprimir_3x4(anno)
                print("\n")
            elif numChoice == 5:
                anno = int(input("\nIngrese un año para imprimir su calendario gregoriano: "))
                imprimir_3x4(anno)
                print("\n")
            elif numChoice == 6:
                print("\nIngrese una fecha para determinar su dia de la semana: ")
                print(dia_semana(pedirFechaAux()))
                print("\n")
            elif numChoice == 7:
                print("\n")
            elif numChoice == 8:
                print("\nIngrese dos fechas para determinar los dias pasados entre ambas: ")
                print(dias_entre(pedirFechaAux(), pedirFechaAux()))
                print("\n")
            elif numChoice == 9:
                print("\nIngrese dos fechas: ")
                edad = edad_al(pedirFechaAux(), pedirFechaAux())
                print("\nAños: ", edad[0], ", meses: ", edad[1], ", días: ", edad[2])
                print("\n")
            elif numChoice == 10:
                print("\nFecha actual: ", fecha_hoy())
                print("\n")
            elif numChoice == 11:
                print("\nIngrese la fecha de nacimiento: ")
                edad = edad_hoy(pedirFechaAux())
                print("\nAños: ", edad[0], ", meses: ", edad[1], ", días: ", edad[2])
                print("\n")
            elif numChoice == 12:
                return
            else:
                print("\nNúmero inválido")

        except:
            print("Caracter Inválido")
        print("***********************************************************************************************")

#mainMenu()