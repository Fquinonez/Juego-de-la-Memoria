# Genera un archivo al terminar el juego
def generar_archivo(nivel, dificultad, j1, jugadas):
    try:
        mensaj = '¡¡¡¡¡Felicidades! Gracias por haber jugado!!!!!\n'
        arch = open('resultado_final.txt', 'wt')
        arch.write(mensaj)
        arch.write(str(j1).upper() + "  ha jugado en modo " + str(dificultad).upper() + " con una matriz de " + str(nivel) + "x" + str(nivel) + '\n')
        arch.write("Usted ganó en " + str(jugadas) + " movimientos.")
    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass


def imprimir_instrucciones():
    print("***************".center(100))
    try:
        arch = open("Instructivo.txt", "rt")
        linea = arch.readline()
        while linea:
            print(linea.rstrip('\n'))
            linea = arch.readline()
    except FileNotFoundError as mensaje:
        print("No se puede acceder a las instrucciones en este momento.", mensaje)
    except OSError as mensaje:
        print("No se puede acceder a las instrucciones en este momento.", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass
    print("***************".center(100))
