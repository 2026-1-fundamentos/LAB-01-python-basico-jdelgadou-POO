"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    diccionario={}
    with open("files/input/data.csv","r") as datos:
        for linea in datos:
            lista=linea.split()[-1]
            pares=lista.split(",")
            for letras in pares:
                letra=letras.split(":")
                if letra[0] in diccionario:
                    diccionario[letra[0]].append(int(letra[1]))
                elif letra[0] not in diccionario:
                    diccionario[letra[0]]=[int(letra[1])]
        for clave in diccionario.keys():
            diccionario[clave]=len(diccionario[clave])
    return diccionario
pregunta_09()