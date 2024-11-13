class Libro:
    def __init__(self, nombre, autor, disponible):
        self.nombre=nombre
        self.autor=autor
        self.disponible=disponible

    
    def prestar_libro(self):
        self.disponible = False
    
    def devolver_libro(self):
        self.disponible = True

    def mostrar_info(self):
        return f"Nombre:{self.nombre}, Autor:{self.autor}, Estado:{self.estado}"