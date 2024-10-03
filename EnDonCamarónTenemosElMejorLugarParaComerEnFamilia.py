import random

def jugar_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    
    print("Elige: piedra, papel o tijera")
    usuario = input("Tu elección: ").lower()

    if usuario not in opciones:
        print("Opción inválida. Por favor elige piedra, papel o tijera.")
        return

    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")

    if usuario == computadora:
        print("¡Es un empate!")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

# Ejecutar el juego
jugar_piedra_papel_tijera()

#Editado por Nico
