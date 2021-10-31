# Crear matriz al azar. Cada elemento debe aparecer dos veces.
from os import system
from manejo_matrices import editar_matriz, comparar_matriz
from manejo_coordenadas import ingresar_coordenadas, interpretar_coordenadas


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
        if comparar_matriz(c1, c2, mat_real, mat_incognita):
            valores_ingresados.extend([c1, c2])
