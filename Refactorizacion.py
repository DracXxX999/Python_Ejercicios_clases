# Ejemplo de codigo a refactorizar:
# Rectangulo 1
base1 = 10
altura1 =5
area1 = base1*altura1
print(f"El area del rectangulo 1 ({base1}x{altura1}) es:{area1} ")

#Rectangulo 2
base2 = 7
altura2 = 3
area2 = base2  * altura2
print (f"El area del rectangulo2 ({base2} * {altura2}) es: {area2}")
def mostrar_area_rectangulo(numero,base,altura):
    area = base * altura 
    print(f"El area del rectangulo {numero} ({base}x{altura}) es: {area}")