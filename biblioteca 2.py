class Libro:
    def __init__(self, autor, titulo, editorial):
        self.autor = autor
        self.titulo = titulo
        self.editorial = editorial
 
    @property
    def autor(self):
        return self._autor
 
    @autor.setter
    def autor(self, autor):
        self._autor = autor
 
    @property
    def titulo(self):
        return self._titulo
 
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
 
    @property
    def editorial(self):
        return self._editorial
 
    @editorial.setter
    def editorial(self, editorial):
        self._editorial = editorial
        
class LibroManager:
    def __init__(self):
        self.libros = []
 
    @property
    def libros(self):
        return self._libros
 
    @libros.setter
    def libros(self, libros):
        self._libros = libros
 
    def agregar(self, libro):
        self.libros.append(libro)
 
    def eliminar(self, indice):
        if indice in range(0, len(self.libros)):
            del self.libros[indice]
 
    def editar(self, indice, libro):
        if indice in range(0, len(self.libros)):
            self.libros[indice].autor = libro.autor
            self.libros[indice].titulo = libro.titulo
            self.libros[indice].editorial = libro.editorial  
class App:
    def __init__(self):
        self.manager = LibroManager()
 
    @property
    def manager(self):
        return self._manager
 
    @manager.setter
    def manager(self, manager):
        self._manager = manager
 
    def menu(self):
 
        while True:
 
            print("")
            print("Elija una opción")
            print("\n1.- Agregar")
            print("2.- Editar")
            print("3.- Listar")
            print("4.- Eliminar")
            print("5.- Salir")
            print("")
 
            try:
                opcion = int(input("?: "))
            except ValueError as ve:
                print("Opción no válida")
                continue
 
            if opcion in range(1, 5):
                self.procesar_opcion(opcion)
            elif opcion == 5:
                break
            else:
                print("Opción no válida")
 
    def procesar_opcion(self, opcion):
 
        if opcion == 1:
            self.agregar()
        elif opcion == 2:
            self.editar()
        elif opcion == 4:
            self.eliminar()
        elif opcion == 3:
            self.listar()
 
    def agregar(self):
 
        titulo = input("\nTitulo: ")
        autor = input("Autor: ")
        editorial = input("Editorial: ")
 
        l = Libro(autor, titulo, editorial)
        self.manager.agregar(l)
 
    def eliminar(self):
 
        self.listar()
 
        try:
 
            indice = int(input("\nIndice del libro: "))
            self.manager.eliminar(indice)
 
        except ValueError as ve:
            print("Indice no válido")
 
    def listar(self):
 
        print("")
 
        for i, l in enumerate(self.manager.libros):
            print("Id: {0}, Autor: {1}, Titulo: {2}, Editorial: {3}".format(i, l.autor, l.titulo, l.editorial))
 
    def editar(self):
 
        self.listar()
 
        try:
 
            indice = int(input("\nIndice del libro: "))
 
            titulo = input("\nNuevo titulo: ")
            autor = input("Nuevo autor: ")
            editorial = input("Nueva editorial: ")
 
            l = Libro(autor, titulo, editorial)
 
            self.manager.editar(indice, l)
            self.listar()
 
        except ValueError as ve:
            print("Indice no válido")
 
 
if __name__ == "__main__":
    app = App()
    app.menu()

     

