def busqueda_binaria(lista, clave):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        print(f"Buscando entre índices {izquierda} y {derecha}, medio: {medio}")

        if lista[medio] == clave:
            return medio  # Éxito: clave encontrada
        elif clave > lista[medio]:
            izquierda = medio + 1  # Buscar en la mitad derecha
        else:
            derecha = medio - 1  # Buscar en la mitad izquierda

    return -1  # Fallo: clave no encontrada


# Ejemplo de uso:
lista_ordenada = [10, 20, 30, 40, 50, 60, 70]
clave = 40

resultado = busqueda_binaria(lista_ordenada, clave)

if resultado != -1:
    print(f"Elemento {clave} encontrado en el índice {resultado}.")
else:
    print(f"Elemento {clave} no encontrado en la lista.")


