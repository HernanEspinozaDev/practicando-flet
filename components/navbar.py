import flet as ft

class Navbar(ft.AppBar):
    def __init__(self):
        super().__init__(
            title=ft.Text("Pastelería", size=20),
            center_title=True,
            bgcolor=ft.colors.SURFACE_VARIANT,
        )
