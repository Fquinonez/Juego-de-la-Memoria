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
    if coord[0].isalpha():
        a = coord[0].lower()
        b = int(coord[1])
    else:
        a = coord[1].lower()
        b = int(coord[0])
    # Creo un diccionario para interpretar a
    letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
    dic_letras = {letras[num]: num for num in range(8)}
    return (dic_letras[a], b - 1)


def limpiar_coordenadas(coord):
    '''Elimina espacios y caracteres no alfanumericos
    del sting que se pasa como parametro.
    Devuelve un string con los caracteres restantes.'''
    coord = coord.lower()
    coord_l = "".join([caracter for caracter in coord if caracter.isalnum()])
    return coord_l


def ingresar_coordenadas(valor_maximo):
    '''El usuario ingresa coordenadas por teclado en
    formato string'''
    msj_error = "Las coordenadas ingresadas son incorrectas.\nEl formato es, por ejemplo, 'A1'."
    coord = input("Ingrese las coordenadas: ")
    # Paso los caracteres a minúsculas, elimino valores no alfanumericos
    coord = limpiar_coordenadas(coord)
    # Valido que las coordenadas tengan dos digitos
    if len(coord) != 2:
        print(msj_error)
        coord = ingresar_coordenadas(valor_maximo)
    # Valido que las coordenadas estén compuestas por una letra y un número
    if coord.isdigit() or coord.isalpha():
        print(msj_error)
        coord = ingresar_coordenadas(valor_maximo)
    # Valido que las coordenadas se encuentren dentro del rango
    c = interpretar_coordenadas(coord)
    c1, c2 = c
    if c1 >= valor_maximo or c2 >= valor_maximo:
        print("El valor ingresado está fuera de rango.")
        coord = ingresar_coordenadas(valor_maximo)
    return coord


def editar_matriz(c1, mat_real, mat_incognita):
    c1f, c1c = c1
    mat_incognita[c1f][c1c] = mat_real[c1f][c1c]
    imprimir_matriz(mat_incognita)


def coomparar_matriz(c1, c2, mat_real, mat_incognita):
    c1f, c1c = c1
    c2f, c2c = c2
    if mat_incognita[c1f][c1c] != mat_real[c2f][c2c]:
        print()
        print("¡Incorrecto!")
        print("")
        sleep(3)
        system("cls")
        mat_incognita[c1f][c1c] = 0
        mat_incognita[c2f][c2c] = 0
        imprimir_matriz(mat_incognita)
        return False
    else:
        print("")
        print("¡Correcto!")
        print("")
        return True


def jugada(jugadas_anteriores, valor_maximo):
    c = ingresar_coordenadas(valor_maximo)
    while interpretar_coordenadas(c) in jugadas_anteriores:
        print("El valor ingresado ya fue encontrado.")
        c = ingresar_coordenadas(valor_maximo)
    return interpretar_coordenadas(c)


def jugar(mat_real, mat_incognita):
    valores_ingresados = []
    val_max = len(mat_real)
    while 0 in [item for fila in mat_incognita for item in fila]:
        # Ingresar coordenadas
        c1 = jugada(valores_ingresados, val_max)
        # Editar matriz
        system("cls")
        editar_matriz(c1, mat_real, mat_incognita)
        # Ingresar coordenadas
        c2 = jugada(valores_ingresados, val_max)
        while c1 == c2:
            print("No se puede ingresar las mismas coordenadas dos veces.")
            c2 = jugada(valores_ingresados, val_max)
        # Editar matriz
        system("cls")
        editar_matriz(c2, mat_real, mat_incognita)
        # Coomparo resultados
        if coomparar_matriz(c1, c2, mat_real, mat_incognita):
            valores_ingresados.extend([c1, c2])
