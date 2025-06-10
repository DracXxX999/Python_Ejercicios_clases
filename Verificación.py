# Ejercicio: Verificador de Edad para Películas usando Funciones

def obtener_clasificacion_pelicula(edad_persona):
    if edad_persona < 0 or edad_persona > 120:
        return "Edad no válida."
    if edad_persona < 13:
        return "Te recomendamos películas G (General Audiences)."
    elif edad_persona < 17:
        return "Puedes ver películas G y PG-13."
    elif edad_persona >= 17:
        return "¡Puedes ver películas de cualquier clasificación incluyendo R!"
    

def main():
    print("=== VERIFICADOR DE EDAD PARA PELÍCULAS ===")
    print()
    
    try:
        edad_ingresada = int(input("Por favor, ingresa tu edad: "))
        
        mensaje_cine = obtener_clasificacion_pelicula(edad_ingresada)
    
        print(f"\nResultado: {mensaje_cine}")
        
    except ValueError:
        print("Error: Por favor ingresa un número válido para la edad.")
    
    print("\n¡Gracias por usar nuestro verificador!")

def probar_multiples_edades():
    """
    Función para probar la función con diferentes edades de ejemplo
    """
    print("\n=== PRUEBAS CON DIFERENTES EDADES ===")
    
    edades_prueba = [5, 12, 13, 16, 17, 25, 65, -5, 150]
    
    for edad in edades_prueba:
        resultado = obtener_clasificacion_pelicula(edad)
        print(f"Edad {edad}: {resultado}")

if __name__== "__main__":
    main()
    print()
    ver_pruebas = input("¿Quieres ver las pruebas con diferentes edades? (s/n): ").lower()
    if ver_pruebas == 's' or ver_pruebas == 'si':
        probar_multiples_edades()