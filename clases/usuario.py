class Usuario:
    def __init__(self, nombre, direccion, telefono):
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.libros= []
    
    def actualizar_info(self, direccion=None, telefono=None):
        if direccion:
            self.direccion=direccion
        if telefono:
            self.telefono=telefono

    def hacer_prestamo(self, libro):
        self.libros.append(libro)
    
    def hacer_devolucion(self, libro):
        self.libros.remove(libro)

    def mostrar_info(self):
        return f"Nombre:{self.nombre}, Direccion:{self.direccion}, Tel.:{self.telefono}"