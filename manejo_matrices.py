import random
from os import system
from time import sleep
from interfaz_grafica import imprimir_matriz


# Matrices
def generar_vacio(n):
    ''' Se genera una matriz cuadrada de
    rango n con ceros.
    Datos de entrada:
        n: Entero
    Datos de salida:
        matriz: Matriz'''
    num = 0
    matriz = []
    for f in range(n):
        # Crear filas
        matriz.append([])
        for c in range(n):
            # Agregar columnas
            matriz[f].append(num)
    return matriz


# Matrices, rebanadas, listas por comprensión
def barajar_cartas(n):
    '''Se genera una matriz de rango n con valores
    numericos que aparecen dos veces.
    Datos de entrada:
        n: Entero
    Datos de salida:
        matriz: Matriz'''
    matriz = []
    cantidad_cartas = (n ** 2) // 2 + 1
    cartas = [carta for carta in range(1, cantidad_cartas)] * 2
    random.shuffle(cartas)
    i = 0
    for f in range(n):
        matriz.append(cartas[i:i + n])
        i += n
    return matriz


def editar_matriz(c1, mat_real, mat_incognita):
    '''Edita el el valor guardado en c1 de matriz incognita
    con el valor guardado en c1 de matriz real.
    Datos de entrada:
        mat_real: Matriz
        mat_incognita: Matriz
        c1: Tupla'''
    c1f, c1c = c1
    mat_incognita[c1f][c1c] = mat_real[c1f][c1c]
    imprimir_matriz(mat_incognita)


def comparar_matriz(c1, c2, mat_incognita):
    '''Compara si dos posiciones de una matriz son iguales.
    Datos de entrada:
        c1: Tupla
        c2: Tupla
        mat_incognita: Matriz'''
    c1f, c1c = c1
    c2f, c2c = c2
    if mat_incognita[c1f][c1c] != mat_incognita[c2f][c2c]:
        print("\n¡Incorrecto!")
        sleep(3)
        system("cls")
        mat_incognita[c1f][c1c] = 0
        mat_incognita[c2f][c2c] = 0
        imprimir_matriz(mat_incognita)
        return False
    else:
        print("\n¡Correcto!")
        return True
