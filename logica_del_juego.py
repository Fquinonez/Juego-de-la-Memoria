# Crear matriz al azar. Cada elemento debe aparecer dos veces.
import random
from os import system
from time import sleep
from interfaz_grafica import imprimir_matriz


# Matrices
def generar_vacio(n):
    ''' Se genera una matriz cuadrada con
    ceros.'''
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
    matriz = []
    cantidad_cartas = (n ** 2) // 2 + 1
    cartas = [carta for carta in range(1, cantidad_cartas)] * 2
    random.shuffle(cartas)
    i = 0
    for f in range(n):
        matriz.append(cartas[i:i + n])
        i += n
    return matriz


# Listas, diccionarios, diccionario por comprensión
def interpretar_coordenadas(coord):
    '''Recibe una cadena de coordendas alfanumerica,
    las interpreta en numeros y las devuelve en forma de tupla'''
    # Separar la coordenada en letra a y numero b
    a = coord[0].lower()
    b = int(coord[1])
    # Creo un diccionario para interpretar a
    letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
    dic_letras = {letras[num]: num for num in range(8)}
    return (dic_letras[a], b - 1)


def ingresar_coordenadas():
    '''El usuario ingresa coordenadas por teclado en
    formato string'''
    coordenadas = input("Ingrese las coordenadas")
    # TODO Restricciones y excepciones
    # TODO No permitir ingresar valores repetidos
    return coordenadas


def editar_matriz(c1, mat_real, mat_incognita):
    c1f = c1[0]
    c1c = c1[1]
    mat_incognita[c1f][c1c] = mat_real[c1f][c1c]
    imprimir_matriz(mat_incognita)


def coomparar_matriz(c1, c2, mat_real, mat_incognita):
    c1f = c1[0]
    c1c = c1[1]
    c2f = c2[0]
    c2c = c2[1]
    if mat_incognita[c1f][c1c] != mat_real[c2f][c2c]:
        print("¡Incorrecto!")
        sleep(3)
        system("cls")
        mat_incognita[c1f][c1c] = 0
        mat_incognita[c2f][c2c] = 0
        imprimir_matriz(mat_incognita)


def jugar(mat_real, mat_incognita):
    while 0 in [item for fila in mat_incognita for item in fila]:
        # Ingresar coordenadas
        c1 = ingresar_coordenadas()
        system("cls")
        # Editar matriz
        editar_matriz(interpretar_coordenadas(c1), mat_real, mat_incognita)
        # Ingresar coordenadas
        c2 = ingresar_coordenadas()
        system("cls")
        # Editar matriz
        editar_matriz(interpretar_coordenadas(c2), mat_real, mat_incognita)
        # Coomparo resultados
        coomparar_matriz(interpretar_coordenadas(c1), interpretar_coordenadas(c2), mat_real, mat_incognita)
