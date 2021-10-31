# Programa principal
from logica_del_juego import jugar
from interfaz_grafica import imprimir_matriz
from manejo_matrices import barajar_cartas, generar_vacio


# Generar matriz real
mat_real = barajar_cartas(4)
mat_incognita = generar_vacio(4)

# Imprimir matriz incognita
imprimir_matriz(mat_incognita)

# Jugar
jugar(mat_real, mat_incognita)
