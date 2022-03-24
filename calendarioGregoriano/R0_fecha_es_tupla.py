

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

def bisiesto(tupla):
    return False

"""
    R2: Verifica si una fecha es válida en el Calendario Gregoriano
"""
def fecha_es_valida(tupla):
    if fecha_es_tupla(tupla):
        if(tupla[0] == 1582):  
            if tupla[1] >= 10 and tupla[2] >= 15 and tupla[2] <= 31:    
                print("La fecha ingresada es válida")
                return True
            else:
                print("La fecha ingresada no es válida en el Calendario Gregoriano para el año 1582")
                return False
        elif tupla[0] > 1582:
            if dia_es_valido(tupla):
                print("La fecha ingresada es válida")
                return True
            else:
                print("La fecha ingresada no es válida en el Calendario Gregoriano.")
                return False
        else:
            print('El año ingresado no es válido en el Calendario Gregoriano')
            return False
    else:
        print ("La fecha debe ser ingresada como una tupla de enteros con formato (año, mes, día)")
        return False

"""
    Verifica si el día ingresado es válido según el mes ingresado 
    y si el año es bisiesto o no.
"""
def dia_es_valido(tupla):
    mes31 = [1, 3, 5, 7, 8, 10, 12] # meses que tienen 31 días
    mes30 = [4, 6, 9, 11]           # meses que tienen 30 días
    mesbisiesto = [2]               # meses que pueden ser bisiesto

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

# tupla = (5,6,7)
# fecha_es_tupla(tupla)