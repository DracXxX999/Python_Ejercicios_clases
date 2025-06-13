def acumulador_suma(lista_numeros):
    lista_numeros = [1, 2, 3, 4, 5]
    acumulador_suma = 0
    for elemento_actual in lista_numeros: 
        acumulador_suma += elemento_actual
    return acumulador_suma
print(acumulador_suma([1, 2, 3, 4, 5]))