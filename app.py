import flet as ft
from views.home_view import HomeView

def main(page: ft.Page):
    page.title = "Pastelería"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Añadir la barra de navegación
    from components.navbar import Navbar
    navbar = Navbar()
    page.appbar = navbar

    # Mostrar la vista principal (HomeView)
    home_view = HomeView()
    page.controls.append(home_view)

    page.update()

if __name__ == "__main__":
    ft.app(target=main)
