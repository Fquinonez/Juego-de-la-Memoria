# Recursividad, listas, rebanadas
def imprimir_lista(lista):
    if len(lista) > 0:
        print('%5d' % lista[0], end=" ")
        imprimir_lista(lista[1:])


def imprimir_lista_color(lista):
    azul = '\033[94m'
    blanco = '\033[0m'
    if len(lista) > 0:
        print(f"{azul}{'%5d' % lista[0]}{blanco}", end=" ")
        imprimir_lista_color(lista[1:])


# Recursividad, listas, rebanadas, matrices
def imprimir_lista_string(matriz, i=0):
    azul = '\033[94m'
    blanco = '\033[0m'
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    if len(matriz) > 0:
        print(f"{azul}{'%6s' % letras[i]}{blanco}", end='')
        imprimir_lista(matriz[0])
        print()
        imprimir_lista_string(matriz[1:], i + 1)


# Recursividad, matrices, rebanadas
def imprimir_matriz(matriz):
    imprimir_lista_color([num for num in range(len(matriz) + 1)])
    print()
    imprimir_lista_string(matriz)
