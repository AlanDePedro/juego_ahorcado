

import random


def obtener_palabra_secreta() -> str: 
    palabras = ["python", "javascript", "java", "angular", "django", "tensorflow", "react", "typescript", "git", "flask"]
    return random.choice(palabras)

def mostrar_progreso(palabra_sacreta, letras_adivinadas):
    adivinado = ""

    for letra in palabra_sacreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado

def juego_ahorcado():
    palabra_sacreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 10
    juego_terminado = False

    print("¡Bienvenido al juego del ahorcado!")
    print(f"tenes {intentos} intentos para descubrir la palabra")
    print(mostrar_progreso(palabra_sacreta, letras_adivinadas), "La cantidad de letras de la palabra es:", len(palabra_sacreta))

    while not juego_terminado and intentos > 0:
        adivinanza = input("introduce una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor introduci una letra valida")
        elif adivinanza in letras_adivinadas:
            print("Ya usaste esa letra intenta con otra")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_sacreta:
                print(f"!Perfecto encontraste la letra {adivinanza} esta presente en la palabra ha adivinar¡")
            else:
                intentos -= 1
                print(f"!Oh lo siento pera la letra {adivinanza} no esta en la palabra secreta¡")
                print(f"Te quedan {intentos} intentos")

        progreso_actual = (mostrar_progreso(palabra_sacreta, letras_adivinadas))
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            palabra_sacreta = palabra_sacreta.capitalize()
            print(f"!FELICIDADES¡ la palabra es: {palabra_sacreta} la descubriste, te quedaron {intentos}")

    if intentos == 0:
        palabra_sacreta = palabra_sacreta.capitalize()
        print(f"Oh en esta oportunidad no adivinaste la palabra que era {palabra_sacreta}")

juego_ahorcado()
