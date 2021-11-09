from os import system
from archivo import imprimir_instrucciones


# Recursividad, listas, rebanadas
def imprimir_lista(lista):
    '''Imprime una lista por consola.'''
    if len(lista) > 0:
        print('%5d' % lista[0], end=" ")
        imprimir_lista(lista[1:])


# Recursividad
def imprimir_lista_color(lista):
    '''Imprime una lista por consola
    en color azul.'''
    azul = '\033[94m'
    blanco = '\033[0m'
    if len(lista) > 0:
        print(f"{azul}{'%5d' % lista[0]}{blanco}", end=" ")
        imprimir_lista_color(lista[1:])


# Recursividad, listas, rebanadas, matrices
def imprimir_lista_string(matriz, i=0):
    '''Imprime una lista por consola. La primera columan contiene
    caracteres en color azul.'''
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
    '''Imprime una matriz con guias alfanumericas en color azul
    como primera fila y columna.'''
    imprimir_lista_color([num for num in range(len(matriz) + 1)])
    print()
    imprimir_lista_string(matriz)


def bienvenida():
    opcion = 0
    bienvenida = '¡¡Bienvenid@ al juego de la MEMORIA!!'
    print(bienvenida.center(50, ' '))
    print()
    print()
    print("¿Estas list@ para jugar? ¡Mucha suerte!")
    print()
    print("Aqui vamos...")
    print()
    print()
    while opcion != 2:
        print("1. Instrucciones del juego")
        print("2. Continuar")
        opcion = int(input("Seleccione una opción."))
        if opcion == 1:
            imprimir_instrucciones()
    system("cls")
