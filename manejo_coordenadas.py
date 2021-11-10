# Listas, diccionarios, diccionario por comprensión, tuplas, excepciones
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
    try:
        coordenadas = (letras.index(a), b - 1)
    except ValueError:
        coordenadas = (9, 9)
    return coordenadas


# Listas por comprension
def limpiar_coordenadas(coord):
    '''Elimina espacios y caracteres no alfanumericos
    del string que se pasa como parametro.
    Devuelve un string con los caracteres restantes.'''
    coord = coord.lower()
    coord_l = "".join([caracter for caracter in coord if caracter.isalnum()])
    return coord_l


def ingresar_coordenadas(valor_maximo):
    '''El usuario ingresa coordenadas por teclado en
    formato string. Devuelve string.
    Datos de entrada:
        valor_maximo: Entero
    Datos de salida:
        coord: String'''
    msj_error = "Las coordenadas ingresadas son incorrectas.\nEl formato es, por ejemplo, 'A1'."
    coord = input("\nIngrese las coordenadas: ")
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
    if c1 not in range(0, valor_maximo) or c2 not in range(0, valor_maximo):
        print("El valor ingresado está fuera de rango.")
        coord = ingresar_coordenadas(valor_maximo)
    return coord
