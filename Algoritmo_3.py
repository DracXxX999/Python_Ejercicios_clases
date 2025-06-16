# Ejercicio 3: Función para contar cuántas veces aparece un elemento en una lista.
# Definición de la función contar_apariciones
def contar_apariciones(lista, elemento_buscado):
    """
    Cuenta cuántas veces aparece un elemento en una lista.

    Parámetros:
        lista: La lista en la que se buscará.
        elemento_buscado: El elemento que queremos contar.

    Retorna:
        El número de veces que el elemento aparece en la lista.
    """
    # Inicialización del contador
    contador = 0

    # Iteración y comparación
    for elemento in lista:
        if elemento == elemento_buscado:
            contador += 1

    # Resultado final
    return contador

# Pruebas del programa
print("\nProbando contar_apariciones...\n")

# Lista de ejemplo
lista_ejemplo = [4, 2, 4, 3, 4, 5, 6, 2, 4, 7, 8, 4]

# Elementos a buscar
elementos_a_buscar = [4, 2, 9, 7]

# Ejecutar pruebas e imprimir resultados
for elemento in elementos_a_buscar:
    resultado = contar_apariciones(lista_ejemplo, elemento)
    print(f"Elemento '{elemento}' aparece {resultado} veces en la lista: {lista_ejemplo}")
print("\nJIMMY REQUENA - FIN DEL PROGRAMA QUE CUENTA LAS VECES QUE APARECE UN ELEMENTO")