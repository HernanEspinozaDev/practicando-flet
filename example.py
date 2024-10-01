import flet as ft

def main(page: ft.Page):
    page.title = "Ejemplo Flet"
    page.add(ft.Text("Hola, este es un ejemplo simple de Flet."))
    page.update()

ft.app(target=main)  # No es necesario especificar 'WEB_BROWSER'
