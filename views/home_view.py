import flet as ft
from viewmodels.pastel_viewmodel import PastelViewModel

class HomeView(ft.Column):
    def __init__(self):
        super().__init__()

        # Inicializar el ViewModel
        self.pastel_vm = PastelViewModel()
        pasteles = self.pastel_vm.fetch_pasteles()

        # Título
        self.controls.append(
            ft.Text("Bienvenido a la Pastelería", size=30, weight=ft.FontWeight.BOLD)
        )

        # Mostrar los pasteles
        for pastel in pasteles:
            self.controls.append(self.create_pastel_card(pastel))

    def create_pastel_card(self, pastel):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(pastel.nombre, size=25, weight=ft.FontWeight.BOLD),
                        ft.Text(pastel.descripcion),
                        ft.Text(f"Precio: ${pastel.precio}"),
                        ft.Text(f"Stock: {pastel.stock} unidades"),
                    ],
                ),
                padding=ft.padding.all(10),
            ),
        )
