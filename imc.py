def main(page: ft.Page):

    nombre = ft.text("Usuario")
    edad = ft.text()
    altura = ft.text()
    peso = ft.text()
    imc = ft.text("0")

    a = ft.text(
        value = f"Buen dia{nombre.value}, su IMC es: {imc.value}"

        
    )