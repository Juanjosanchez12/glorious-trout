def invertir_cadena(cadena):
    """
    Esta función toma una cadena como entrada y devuelve la misma cadena invertida.

    Args:
        cadena (str): La cadena de entrada.

    Returns:
        str: La cadena de entrada invertida.
    """
    return cadena[::-1]

print(invertir_cadena("Hola Mundo"))

# Crea una funcion que devuelva la longitud de una cadena
def longitud_cadena(cadena):
    """
    Esta función toma una cadena como entrada y devuelve su longitud.

    Args:
        cadena (str): La cadena de entrada.

    Returns:
        int: La longitud de la cadena de entrada.
    """
    return len(cadena)

print(longitud_cadena("Hola Mundo"))

def contar_consonantes(cadena):
    """
    Esta función toma una cadena como entrada y devuelve el número de consonantes en la cadena.

    Args:
        cadena (str): La cadena de entrada.

    Returns:
        int: El número de consonantes en la cadena.
    """
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in cadena if char in consonantes)

print(contar_consonantes("Hola Mundo"))
