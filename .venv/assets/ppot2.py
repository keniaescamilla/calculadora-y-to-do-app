import flet as ft
import random

def main(page: ft.Page):
    page.add(
    t = ft.Text(value="ELIGE PIEDRA PAPEL O TIJERA", color="pink")
    )
    opciones = ["piedra", "papel", "tijera"]
    opcion_compu = random.choice(opciones)
    usuario = input("piedra, papel o tijera: ").lower()
    if usuario not in opciones:
        print("Elige una opción válida")
        return
    print(f"Tu: {usuario}")
    print(f"Compu: {opcion_compu}")
    if usuario == opcion_compu:
        print("Empate")
    elif (usuario == "piedra" and opcion_compu == "tijera") or (usuario == "papel" and opcion_compu == "piedra") or (usuario == "tijera" and opcion_compu == "papel"):
        print("Eres un ganador")
    else:
        print("Eres perdedor!")

ft.app(target=main)
