
from clases.libro import Libro
from clases.usuario import Usuario


def registrar_libro():
    nombre=input("Titulo del libro: ")
    autor=input("Autor del libro: ")
    disponible=True
    libro=Libro(nombre, autor, disponible)
    return libro

def registrar_usuario():
    nombre=input("Nombre de Usuario: ")
    direccion=input("Direccion: ")
    telefono=input("Tel.: ")
    usuario=Usuario(nombre, direccion, telefono)
    return usuario

def registrar_prestamo(usuarios, biblioteca):
    nombre_usuario=input("Digame el nombre de ususario: ")
    usuario=next((u for u in usuarios if u.nombre == nombre_usuario), None)

    # if usuario not in usuarios:
    #     print("El usuario no existe")
    
    while True:
        nombre_libro=input("Cual es el nombre del libro que desea (no ponga nada si desea terminar): ")
        # if not nombre_libro:
        #     break

        libro=next((lib for lib in biblioteca if lib.nombre==nombre_libro), None)

        if not libro:
            print("Disculpa no tenemos ese libro")
        elif not libro.disponible:
            print("Disculpa, ese libro no esta disponible en este momento")
        elif libro.disponible:
            print("Ese libro esta disponible")
            libro.prestar_libro()
            usuario.hacer_prestamo()
    

def main():
    usuarios=[]
    op=input("Ingrese una opcion: ")
    biblioteca=[]

    while True:
        if op=="1":
            libro = registrar_libro()
            if libro:
                biblioteca.append(libro)
                print("Se ha registrado con exito")
        elif op=="2":
            usuario= registrar_usuario()
            if usuario:
                usuarios.append(usuario)
                print("Se ha registrado con exito")
        elif op=="3":
            registrar_prestamo(usuarios, biblioteca)
        elif op=="4":
            print(biblioteca)

main()




