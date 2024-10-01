# views/index.py
import flet as ft

class IndexView:
    def __init__(self):
        pass

    def build(self, page):
        page.add(ft.Text("Bienvenido a la Tienda de Pasteles"))
        
        # Definir la acción del botón
        def go_to_home(e):
            page.go("/home")  # Navegar a la página home

        # Crear un botón que redirige a la página home
        home_button = ft.ElevatedButton(text="Ir a la tienda", on_click=go_to_home)
        
        # Añadir el botón a la página
        page.add(home_button)
