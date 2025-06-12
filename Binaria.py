# clase06_busquedas.py (Continuación o en un nuevo archivo si así lo prefieres)

def busqueda_binaria(lista_ordenada, clave):
    """
    Implementa el algoritmo de búsqueda binaria "Divide y Vencerás".

    Args:
        lista_ordenada (list): La lista ordenada en la que buscar.
        clave: El elemento a buscar.

    Returns:
        int: El índice de la clave si se encuentra, o -1 si no.
    """
    # Inicializa izquierda = 0 y derecha = len(lista_ordenada) - 1.
    izquierda = 0
    derecha = len(lista_ordenada) - 1

    # Inicia un bucle while izquierda <= derecha:.
    while izquierda <= derecha:
        # Dentro del bucle:
        # medio = (izquierda + derecha) // 2.
        medio = (izquierda + derecha) // 2

        # if lista_ordenada[medio] == clave: return medio.
        if lista_ordenada[medio] == clave:
            return medio
        # elif clave > lista_ordenada[medio]: izquierda = medio + 1.
        elif clave > lista_ordenada[medio]:
            izquierda = medio + 1
        # else: derecha = medio - 1.
        else:  # clave < lista_ordenada[medio]
            derecha = medio - 1

    # Si el bucle termina, return -1.
    return -1

# Prueba tu función:
if __name__ == "__main__":
    lista_ordenada = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

    print("\nProbando busqueda_binaria...")

    # Test cases using assert
    assert busqueda_binaria(lista_ordenada, 23) == 5, "Test Falló: 23 debería estar en el índice 5"
    assert busqueda_binaria(lista_ordenada, 91) == 9, "Test Falló: 91 debería estar en el último índice"
    assert busqueda_binaria(lista_ordenada, 2) == 0, "Test Falló: 2 debería estar en el primer índice"
    assert busqueda_binaria(lista_ordenada, 3) == -1, "Test Falló: 3 no debería existir"
    assert busqueda_binaria(lista_ordenada, 100) == -1, "Test Falló: 100 no debería existir (fuera de rango mayor)"
    assert busqueda_binaria([], 5) == -1, "Test Falló: Búsqueda binaria en lista vacía"
    assert busqueda_binaria([1], 1) == 0, "Test Falló: Búsqueda binaria con un solo elemento encontrado"
    assert busqueda_binaria([1], 99) == -1, "Test Falló: Búsqueda binaria con un solo elemento no encontrado"


    print("¡Pruebas para busqueda_binaria pasaron! ✅")

    # Optional: Additional test cases
    print("\nEjemplos adicionales:")
    print(f"Buscando 12 en {lista_ordenada}: {busqueda_binaria(lista_ordenada, 12)}")
    print(f"Buscando 5 en {lista_ordenada}: {busqueda_binaria(lista_ordenada, 5)}")
    print(f"Buscando 70 en {lista_ordenada}: {busqueda_binaria(lista_ordenada, 70)}")