import flet as ft

def main (page:ft.Page):
    page.window_width = 850
    page.window_height = 850
    page.scroll_to = True
    page.window_title = "Jugar piedra, papel o tijera"

ft.app(target=main)

