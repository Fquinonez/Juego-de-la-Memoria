# Programa principal
from logica_del_juego import jugar, configurar_juego
from interfaz_grafica import imprimir_matriz, bienvenida
from manejo_matrices import barajar_cartas, generar_vacio
from archivo import generar_archivo

# Bienvenida
bienvenida()

# Configurar las caracteristicas del jugador y juego
nivel_juego, nombre_jugador, dificultad_juego = configurar_juego()

# Generar matriz real
mat_real = barajar_cartas(nivel_juego)
mat_incognita = generar_vacio(nivel_juego)

# Imprimir matriz incognita
imprimir_matriz(mat_incognita)

# Jugar
cant_movidas = jugar(mat_real, mat_incognita)

# Generar archivo y terminar juego
generar_archivo(nivel_juego, dificultad_juego, nombre_jugador, cant_movidas)
print()
print("¡El juego finalizó!")
print()
print("Se creó un archivo llamado 'Resultados Final', en el cual\npodras ver la cantidad de movimientos realizados para\ncompletar el juego. El archivo se creó en la misma dirección\ndonde se encuentra el juego")
