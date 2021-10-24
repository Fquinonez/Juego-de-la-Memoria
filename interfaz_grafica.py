# Recursividad, listas, rebanadas
def imprimir_lista(lista):
    if len(lista) > 0:
        print("%5d" % lista[0], end=" ")
        imprimir_lista(lista[1:])


# Recursividad, matrices, rebanadas
def imprimir_matriz(matriz):
    # TODO: Imprimir coordenadas
    if len(matriz) > 0:
        imprimir_lista(matriz[0])
        print("")
        imprimir_matriz(matriz[1:])
