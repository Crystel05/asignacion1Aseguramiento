

def fecha_es_tupla(paramFecha):

    if isinstance(paramFecha, tuple):
        if len(paramFecha) == 3:
            for item in paramFecha:
                if not isinstance(item, int) or item < 0:
                    print("La tupla introducida contiene items no numerales o menores a 0")
                    return False
            return True
        else:
            print("La canditad de items en la tupla es diferente de 3 \n")
            return False
    else:
        print("El parametro introducido no es una tupla \n")
        return False


# tupla = (5,6,7)
# fecha_es_tupla(tupla)