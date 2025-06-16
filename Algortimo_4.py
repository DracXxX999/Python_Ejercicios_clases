# Ejercicio 4: Función para invertir la posiciòn de los elementos de una lista
# Definición de la función invertir_lista
def invertir_lista(lista_original):
    """
    Recibe una lista y retorna una nueva lista con los elementos en orden inverso.
    No modifica la lista original.
    """
    lista_invertida = []

    # Recorrer la lista original de atrás hacia adelante
    for i in range(len(lista_original) - 1, -1, -1):
        lista_invertida.append(lista_original[i])

    return lista_invertida

# Pruebas de la función
print("\nProbando invertir_lista...\n")

# Lista de prueba
lista_prueba = [1, 2, 3, 4, 5]
lista_resultante = invertir_lista(lista_prueba)

# Imprimir resultados
print(f"Lista original: {lista_prueba}")
print(f"Lista invertida: {lista_resultante}")

# Asserts para verificar comportamiento correcto
assert lista_resultante == [5, 4, 3, 2, 1]
assert lista_prueba == [1, 2, 3, 4, 5]  # La lista original no debe cambiar
assert invertir_lista(["a", "b", "c"]) == ["c", "b", "a"]
assert invertir_lista([]) == []

print("¡Pruebas para invertir_lista pasaron! ✅")
print("\nMarco Aurelio - FIN DEL PROGRAMA QUE INVIERTE LOS ELEMENTOS DE UNA LISTA")

