# views/pastel_view.py

import flet as ft
from viewmodels.pastel_viewmodel import PastelViewModel

class PastelView:
    def __init__(self, vm: PastelViewModel):
        self.vm = vm

    def build(self, page):
        def login_user(e):
            self.vm.login(username_input.value, password_input.value)
            page.update()

        username_input = ft.TextField(label="Usuario")
        password_input = ft.TextField(label="Contraseña", password=True)
        login_button = ft.ElevatedButton(text="Iniciar sesión", on_click=login_user)

        page.add(username_input, password_input, login_button)

    def display_pasteles(self, page):
        pasteles = self.vm.fetch_pasteles()
        for pastel in pasteles:
            page.add(ft.Text(f"Nombre: {pastel[1]}, Precio: {pastel[3]}, Stock: {pastel[4]}"))
