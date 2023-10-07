import flet as ft
import random
def ppot():
    opciones = ["piedra", "papel", "tijera"]
    opcion_compu= random.choice(opciones)
    usuario = input("peidra papel o tijeira").lower()
    if usuario not in opciones:
        print("Elige una opcion valida")
        return
    print(f"Tu:{usuario}")
    print(f"Compu: {opcion_compu}")
    if usuario == opcion_compu:
        print("empate")
    elif(usuario == "piedra" and opcion_compu == "tijera") or (usuario == "papel" and opcion_compu == "piedra") or (usuario == "tijera" and opcion_compu == "papel"):
        print("eres un ganador")
    else:
        print("Eres perdedor!")
ppot()
