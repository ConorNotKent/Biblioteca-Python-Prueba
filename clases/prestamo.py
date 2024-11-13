
class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario=usuario
        self.libro=libro
    
    def registrar_prestamo(self):
        return f"Usuario {self.usuario} tiene {self.libro}"