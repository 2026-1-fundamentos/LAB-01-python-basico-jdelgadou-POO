"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    diccionario={}
    with open("files/input/data.csv","r") as datos:
        for linea in datos:
            lista=linea.split()
            letra=lista[0]
            if letra in diccionario:
                diccionario[letra].append(int(lista[1]))
            elif letra not in diccionario:
                diccionario[letra]=[int(lista[1])]
    return [(letra,max(valores), min(valores)) for letra, valores in sorted(diccionario.items())]
pregunta_05()