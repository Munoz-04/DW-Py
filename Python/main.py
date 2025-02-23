import random
import time

def elegir_opcion(opciones):
    """Función para pedir al usuario una opción válida."""
    while True:
        try:
            opcion = int(input("Elige una opción: "))
            if opcion not in opciones:
                raise ValueError("Opción no válida. Intenta de nuevo.")
            return opcion
        except ValueError as e:
            print(f"❌ Error: {e}")

def batalla(enemigo, vida_jugador):
    """Simula una batalla entre el jugador y un enemigo."""
    print(f"\n⚔️ ¡Un {enemigo} aparece! Prepárate para la batalla.")
    vida_enemigo = random.randint(10, 30)
    
    while vida_jugador > 0 and vida_enemigo > 0:
        try:
            print(f"\nTu vida: ❤️ {vida_jugador} | Vida del {enemigo}: 💀 {vida_enemigo}")
            ataque = int(input("📌 Elige tu ataque (1: Golpe rápido ⚡ | 2: Ataque fuerte 💥): "))
            if ataque not in [1, 2]:
                raise ValueError("Debes elegir 1 o 2.")

            if ataque == 1:
                dano = random.randint(5, 10)
            else:
                dano = random.randint(10, 20)

            vida_enemigo -= dano
            print(f"🔥 Has hecho {dano} de daño al {enemigo}!")

            if vida_enemigo > 0:
                dano_recibido = random.randint(5, 15)
                vida_jugador -= dano_recibido
                print(f"💀 El {enemigo} te ataca y te hace {dano_recibido} de daño!")

        except ValueError as e:
            print(f"❌ Error: {e}")

    if vida_jugador > 0:
        print(f"\n🎉 ¡Has derrotado al {enemigo}!")
        return vida_jugador
    else:
        print("\n☠️ Has sido derrotado... Fin del juego.")
        exit()

def juego():
    """Función principal del juego."""
    vida_jugador = 50
    print("\n🏰 Bienvenido a LA MAZMORRA DEL DRAGÓN 🐉")
    time.sleep(1)
    print("\nEstás en la entrada de una antigua mazmorra llena de peligros y tesoros.")
    
    print("\n¿Qué deseas hacer?")
    print("1️⃣ Entrar a la mazmorra")
    print("2️⃣ Huir como un cobarde 🏃")
    
    opcion = elegir_opcion([1, 2])
    
    if opcion == 2:
        print("\n😆 Decidiste huir. Tal vez la aventura no es para ti. Fin del juego.")
        return
    
    print("\n🔦 Entras a la mazmorra y ves dos caminos:")
    print("1️⃣ Camino oscuro y tenebroso.")
    print("2️⃣ Camino iluminado con antorchas.")
    
    opcion = elegir_opcion([1, 2])
    
    if opcion == 1:
        print("\n👻 Un goblin te ataca en la oscuridad!")
        vida_jugador = batalla("Goblin", vida_jugador)
    else:
        print("\n💰 Encuentras un cofre con una poción! Ganas 20 de vida.")
        vida_jugador += 20
    
    print("\n⛓️ Sigues avanzando y llegas a una gran puerta.")
    print("1️⃣ Abrir la puerta y entrar.")
    print("2️⃣ Buscar otra salida.")

    opcion = elegir_opcion([1, 2])

    if opcion == 2:
        print("\n🚷 El techo se derrumba y quedas atrapado... Fin del juego.")
        return
    
    print("\n🔥 Dentro de la sala, un DRAGÓN aparece! 🐉")
    vida_jugador = batalla("Dragón", vida_jugador)
    
    print("\n🎉 ¡Felicidades! Has derrotado al Dragón y encontrado el tesoro. ¡Eres una leyenda! 🏆")

# Ejecutar el juego
juego()
