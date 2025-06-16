#Adivinar número secreto
numero_secreto = 7
adivinanza = int(input("Adivina el número secreto entre 1 y 10: "))
while adivinanza != numero_secreto:
    if adivinanza < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    else:
        print("Demasiado alto. Intenta de nuevo.")
    adivinanza = int(input("Adivina otra vez: "))
print(f"¡Correcto! El número era {numero_secreto}.")