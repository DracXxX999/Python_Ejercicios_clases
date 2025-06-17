def ordenamiento_burbuja(lista):
    n = len(lista) # Cantidad de elementos en la lista
    for i in range(n - 1): # Bucle exterior para las pasadas
        hubo_intercambio = False # Marca si hubo un intercambio en esta pasada
        for j in range(n - 1 - i): # Cada pasada evita revisar los últimos ya ordenados
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_intercambio = True
        if not hubo_intercambio: # Si no hubo ningún intercambio, la lista ya está ordenada
            break

# Main
if __name__ == "__main__":
    # Prueba 1
    numeros = [6, 3, 8, 2, 5]
    print("Antes:", numeros)
    ordenamiento_burbuja(numeros)
    print("Después:", numeros)
    
    # Prueba 2
    lista_a_ordenar = [64, 34, 25, 12, 22, 11, 90]
    print(f"Lista original: {lista_a_ordenar}")
    ordenamiento_burbuja(lista_a_ordenar)
    print(f"Lista ordenada: {lista_a_ordenar}")

    # Casos de prueba con assert
    # Caso 1: Lista desordenada
    lista1 = [6, 3, 8, 2, 5]
    ordenamiento_burbuja(lista1)
    assert lista1 == [2, 3, 5, 6, 8], "Fallo en Caso 1"
    
    # Caso 2: Lista ya ordenada
    lista2 = [1, 2, 3, 4, 5]
    ordenamiento_burbuja(lista2)
    assert lista2 == [1, 2, 3, 4, 5], "Fallo en Caso 2"
    
    # Caso 3: Lista ordenada a la inversa (peor caso)
    lista3 = [5, 4, 3, 2, 1]
    ordenamiento_burbuja(lista3)
    assert lista3 == [1, 2, 3, 4, 5], "Fallo en Caso 3"
    
    # Caso 4: Lista con elementos duplicados
    lista4 = [5, 1, 4, 2, 8, 5, 2]
    ordenamiento_burbuja(lista4)
    assert lista4 == [1, 2, 2, 4, 5, 5, 8], "Fallo en Caso 4"
    
    # Casos borde
    lista_vacia = []
    ordenamiento_burbuja(lista_vacia)
    assert lista_vacia == [], "Fallo en lista vacía"
    
    lista_un_elemento = [42]
    ordenamiento_burbuja(lista_un_elemento)
    assert lista_un_elemento == [42], "Fallo en lista con un elemento"
    
    print("¡Todas las pruebas pasaron!")