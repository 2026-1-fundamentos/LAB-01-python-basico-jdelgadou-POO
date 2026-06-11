"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    diccionario={}
    with open("files/input/data.csv","r") as datos:
        for linea in datos:
            lista=linea.split()
            lista_diccionario=linea.split()[-1]
            pares=lista_diccionario.split(",")
            for letras in pares:
                letra=letras.split(":")
                if lista[0] in diccionario:
                    diccionario[lista[0]]+=int(letra[1])
                elif lista[0] not in diccionario:
                    diccionario[lista[0]]=int(letra[1])
    return diccionario
pregunta_12()