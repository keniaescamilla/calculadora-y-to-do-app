import flet as ft
import random

def main(page:ft.Page):
    page.window_width = 850
    page.window_height = 850
    page.scroll_to = True
    page.window_title = "Calcula tu signo zodiacal"
    
    sFechaAcuario = ft.Text("Ganas", style=ft.TextThemeStyle.TITLE_SMALL)
    

    piscis =ft.Column(
        controls=[sPiscis, sFechaPiscis],
        scroll=ft.ScrollMode.ALWAYS
    )
    
    piscis.visible = False
    
    def calcularSigno(e):
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
        page.update()
    elif(usuario == "piedra" and opcion_compu == "tijera") or (usuario == "papel" and opcion_compu == "piedra") or (usuario == "tijera" and opcion_compu == "papel"):
        print("eres un ganador")
        page.update()
    else:
        print("Eres perdedor!")
        page.update()


    inputN = ft.TextField(
            label="Nombre : ",
            width=600)
    btn_calcular = ft.ElevatedButton(
    text="Calcular",
    bgcolor=ft.colors.BLUE_GREY_100,
    color=ft.colors.BLACK,
    expand=1,
    on_click= calcularSigno,
    width=100,
    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), ),
    )
    r1= ft.Row(
        controls=[inputN]
    )

    page.add(
        
        ft.Text(
            spans=[
                ft.TextSpan(
                    "Calcula tu signo zodiacal",
                    ft.TextStyle(
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        foreground=ft.Paint(gradient=ft.PaintLinearGradient(
                                (0, 20), (150, 20), [ft.colors.BLUE_GREY_100, ft.colors.BLUE_GREY_900]
                            )
                        ),
                    ),
                ),
            ],
        )
    )
    page.add(r1, r2, r3)
    page.add(
        tauro,
        aries,
        geminis,
        cancer,
        leo,
        virgo,
        libra,
        escorpio,
        sagitario,
        capricornio,
        acuario,
        piscis
    )
    
ft.app(target=main)