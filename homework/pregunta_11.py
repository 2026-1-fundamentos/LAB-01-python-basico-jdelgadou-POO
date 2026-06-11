"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    diccionario={}
    with open("files/input/data.csv","r") as datos:
        for linea in datos:
            lista=linea.split()
            lista_letras=lista[-2]
            pares=lista_letras.split(",")
            for letra in pares:
                if letra in diccionario:
                    diccionario[letra]+=int(lista[1])
                elif letra not in diccionario:
                    diccionario[letra]=int(lista[1])
    return diccionario
pregunta_11()