# Ejercicio 2: Función para encontrar el mayor elemento de una lista
# Definición de la función encontrar_mayor

def encontrar_mayor(lista_numeros):
    """
    Recibe una lista de números y retorna el número más grande.
    Si la lista está vacía, retorna None.
    """
    # Caso especial: lista vacía
    if not lista_numeros:
        return None

    # Inicializar con el primer elemento
    mayor_temporal = lista_numeros[0]

    # Recorrer el resto de la lista
    for elemento_actual in lista_numeros[1:]:
        if elemento_actual > mayor_temporal:
            mayor_temporal = elemento_actual

    # Devolver el mayor encontrado
    return mayor_temporal

# Pruebas de la función con impresión de resultados
print("\nProbando encontrar_mayor...\n")

listas_de_prueba = [
    [1, 9, 2, 8, 3, 7],
    [-1, -9, -2, -8],
    [42, 42, 42],
    [],
    [5]
]

# Ejecutar cada prueba y mostrar resultados
for lista in listas_de_prueba:
    resultado = encontrar_mayor(lista)
    print(f"Lista: {lista} -> Mayor encontrado: {resultado}")

# Verificar que los resultados son correctos con assert
assert encontrar_mayor([1, 9, 2, 8, 3, 7]) == 9
assert encontrar_mayor([-1, -9, -2, -8]) == -1
assert encontrar_mayor([42, 42, 42]) == 42
assert encontrar_mayor([]) == None
assert encontrar_mayor([5]) == 5

print("\n¡Pruebas para encontrar_mayor pasaron! ✅")

print("\nMarco Aurelio - FIN DEL PROGRAMA ENCUENTRA EL MAYOR ELEMENTO")