import flet as ft

def main(page: ft.Page):
    Page.title ="Basic elevated buttons"
    Page.add(
        ft.ElevatedButton(text="Eevated button"),
        ft.ElevatedButton("disabled button",disabled=True),
        

    )
    def button_clicked(e):
        b.data += 1
        t.value = f"Button clicked {b.data} time(s)"
        page.update()

        b= ft.ElevatedButton("Button with clcik event", on_click=button_clicked, data=0)
        t= ft.text()

        page.add(b, t)
ft.app(target = main)