# Crear matriz al azar. Cada elemento debe aparecer dos veces.
from os import system
from manejo_matrices import editar_matriz, comparar_matriz
from manejo_coordenadas import ingresar_coordenadas, interpretar_coordenadas


def jugada(jugadas_anteriores, valor_maximo):
    '''Se ingresan coordenadas en formato string. Se devuelven
    en formato tupla.
    Datos de entrada:
        jugadas_anteriores: Lista
        valor_maximo: Entero
    Datos de salida:
        tupla'''
    c = ingresar_coordenadas(valor_maximo)
    while interpretar_coordenadas(c) in jugadas_anteriores:
        print("El valor ingresado ya fue encontrado.")
        c = ingresar_coordenadas(valor_maximo)
    return interpretar_coordenadas(c)


def jugar(mat_real, mat_incognita):
    '''Se ingresan dos coordenadas. Se edita la matriz incognita en caso de acierto.
    Se ejecuta hasta descubrir todos los valores de la matriz.
    Datos de entrada:
        mat_real: Matriz
        mat_incognita: Matriz
    Datos de salida:
        movimientos: Entero'''
    valores_ingresados = []
    val_max = len(mat_real)
    movimientos = 0
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
        # Contar movimientos
        movimientos = movimientos + 1
        # Coomparo resultados
        if comparar_matriz(c1, c2, mat_incognita):
            valores_ingresados.extend([c1, c2])
    return movimientos


def configurar_juego():
    '''Se ingresan los datos nombre del jugador y dificultad.
    Datos de salida:
        nivel: Entero
        jugador: String
        dificultad: String'''
    jugador = input("Nombre del jugador: ")
    dificultad = input("Nivel de dificultad (Facil = 4x4 / Medio = 6x6 / Dificil = 8x8): ")
    while dificultad.lower() != 'facil' and dificultad.lower() != 'medio' and dificultad.lower() != 'dificil':
        print("Debe ingresar una dificultad correcta.")
        dificultad = input("Nivel de dificultad( Facil= 4x4 / Medio= 6x6 / Dificil= 8x8)= ")
    if dificultad.lower() == 'facil':
        nivel = 4
    if dificultad.lower() == 'medio':
        nivel = 6
    if dificultad.lower() == 'dificil':
        nivel = 8
    input("Presione enter para continuar.")
    system("cls")
    return int(nivel), jugador, dificultad
