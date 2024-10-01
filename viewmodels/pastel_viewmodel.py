from services.db_service import get_pasteles

class PastelViewModel:
    def __init__(self):
        self.pasteles = []

    def fetch_pasteles(self):
        # Obtener la lista de pasteles desde la base de datos
        self.pasteles = get_pasteles()
        return self.pasteles
