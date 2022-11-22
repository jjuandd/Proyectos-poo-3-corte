#lista de los libros para su respectivo menu
Libro_1 = []
Libro_2 = []
Libro_3 = []
Libro_4 = []
libro_5 = []
libro_6 = []
libro_7 = []
class libros:
    def Menu_de_los_libros(self):
        print(".........................................")
        print("La biblioFET")
        print("Tenemos libros de todo tipo de genero")
        print(".........................................")
        print("Escoja un libro para otorgarle la información de el")
        print(".........................................")
        print("1-Genero de princesas")
        print("2-Genero de accion y guerra ")
        print("3-Genero de reflexion y paz ")
        print("4-Genero de amor")
        print("5-Genero de drama ")
        print("Gracias por escogernos")
        elija = int(input("Cual seria tu eleccion caballero o señorita?: "))
        print(".........................................")
        if elija == 1:
            self.libro1()
        if elija == 2:
            self.libro2()
        if elija == 3:
            self.libro3()
        if elija == 4:
            self.libro_4()
        if elija == 5:
            self.libro_5()
            
class registo_cliente:
    def __init__(self, nombre = 0, apellido= 0, codigo=0,):
        self._nombre = nombre
        self._apellido = apellido
        self._codigo= codigo
    def set_nombre(self, nombre):
        self._nombre = nombre
    def get_nombre(self):
        return self._nombre
    def set_apellido(self, apellido):
        self._apellido = apellido
    def get_apellido(self):
        return self._apellido
    def set_codigo(self, codigo):
        self._codigo =codigo
    def get_codigo(self):
        return self._codigo
            
    def libro1(self):
        Menu=[
            ["titulo:la bella y la bestia"],
            ["Autor: Gabrielle-Suzanne Barbot de Villeneuve"],
            ["# de edicion: 1"],
            ["Fecha de publicación original: 2003"],
            ["Gabrielle-Suzanne Barbot de Villeneuve"],
            ["Género: Cuento"],
            ["Idioma:Español"],
            ["ISBN: 897766664"],
        ]
        for x in range(6):
            print(Menu[x][0])
        self.__init__()
        
    def libro2(self):
        Menu=[
            ["Titulo : El arte de la guerra"],
            ["# de edicion: 1"],
            ["Autor: Sun Tzu"],
            ["Géneros: Tratado, No-ficción"],
            ["Idiomas originales: Chino, Chino clásico"],
            ["ISBN: 8766443211"],
        ]
        for x in range(6):
            print(Menu[x][0])
        self.__init__()
        
        
    def libro3(self):
        Menu=[
            ["Titulo : El ego es el enemigo"],
            ["# de edicion: 5"],
            ["Autor: Ryan Holiday"],
            ["Idioma original: Inglés"],
            ["Géneros: Libro de autoayuda, Ensayo"],
            ["ISBN:990011223"],
            ["Fecha de publicación original: 14 de junio de 2016"],
        ]
        for x in range(6):
            print(Menu[x][0])
        self.__init__()
        
        
    def libro_4(self):
        Menu=[
            ["Titulo : Cumbres Borrascosas"],
            ["Autora: Emily Brontë"],
            ["# de edicion: 7"],
            ["Personajes: Heathcliff, Catherine Earnshaw, Hareton Earnshaw."],
            ["Géneros: Novela, Ficción gótica, Novela rosa, Tragedia"],
            ["Fecha de publicación original: diciembre de 1847"],
            ["ISBN: 877889003"],
        ]
        for x in range(6):
            print(Menu[x][0])
        self.__init__()
    
    def libro_5(self):
        Menu=[
            ["Titulo : las mujeres que aman demasiado"],
            ["Autora: Robin Norwood"],
            ["# de edicion: 2"],
            ["Género: Libro de autoayuda"],
            ["Fecha de publicación original: 1985"],
            ["Idioma original: Inglés"],
            ["ISBN: 18291003"],
        ]
        for x in range(6):
            print(Menu[x][0])
        self.__init__()
    

class libroAprestar(registo_cliente,libros):
    def __init__(self):
        super(libroAprestar,self).__init__()
        print(".........................................")
        print("BIENVENIDO A LA BIBLIOFET")
        print(" 1 = Para poder ver las opciones de libros que tenemos")
        print(" 2 = Por si deseas tomar un libro en posesion ")
        print("Muchas gracias")
        print(".........................................")
        seleccion = int(input("Digita tu opcion por favor: "))
        if seleccion == 1:
            super(libroAprestar,self).Menu_de_los_libros()
        if seleccion == 2:
            libre = registo_cliente()
            libre.set_nombre(input("nombre:  "))
            libre.set_apellido(input("apellido: "))
            libre.set_codigo(input("ingrese su codigo:"))
            print(".........................................")
            print("Estas son algunas opciones de libros que tenemos, como puedes observar son varios")
            print("1 = La bella y la bestia ")
            print("2 = El arte de la guerra ")
            print("3 = El ego es el enemigo ")
            print("4 = Cumbres borrascosas ")
            print("5 = Las mujeres que aman demasiado ")
            print("6 = Inteligencia sexual")
            print("7 = Juego de mentrias")
            print("8 = Salir sin escojer")
            print(".........................................")
            seleccion = int(input(("digite el numero del libro a prestar ")))
            print(".........................................")
            if seleccion == 1:
                if 1 in Libro_1:
                    print("ocupado o no existente")
                    self.__init__()
                else:
                    print(".........................................")
                    print("El libro numero 1 ha sido prestado")
                    print(" al cliente con codigo:", (libre.get_codigo()))
                    print("desde hoy tiene 15 dias habiles para devolverlo")
                    print("en tal caso que no sea asi , usted sera betado")
                    print("muchas gracias")
                    print(".........................................")
                    Libro_1.append(1)
                    self.__init__()
            if seleccion == 2:
                if 1 in Libro_2:
                    print("ocupado o no existente")
                    self.__init__()
                else:
                    print(".........................................")
                    print("El libro numero 2 ha sido prestado")
                    print(" al cliente con codigo:", (libre.get_codigo()))
                    print("desde hoy tiene 15 dias habiles para devolverlo")
                    print("en tal caso que no sea asi , usted sera betado")
                    print("muchas gracias")
                    print(".........................................")
                    Libro_2.append(2)
                    self.__init__()
            if seleccion == 3:
                if 1 in Libro_3:
                    print("ocupado o no existente")
                    self.__init__()
                else:
                    print(".........................................")
                    print("El libro numero 3 ha sido prestado")
                    print(" al cliente con codigo:", (libre.get_codigo()))
                    print("desde hoy tiene 15 dias habiles para devolverlo")
                    print("en tal caso que no sea asi , usted sera betado")
                    print("muchas gracias")
                    print(".........................................")
                    Libro_3.append(1)
                    self.__init__()
            
            if seleccion == 4:
                if 1 in Libro_4:
                    print("ocupado o no existente")
                    self.__init__()
                else:
                    print(".........................................")
                    print("El libro numero 4 ha sido prestado")
                    print(" al cliente con codigo:", (libre.get_codigo()))
                    print("desde hoy tiene 15 dias habiles para devolverlo")
                    print("en tal caso que no sea asi , usted sera betado")
                    print("muchas gracias")
                    print(".........................................")
                    Libro_4.append(1)
                    self.__init__()
                    
            if seleccion == 5:
                if 1 in libro_5:
                    print("ocupado o no existente")
                    self.__init__()
                else:
                    print(".........................................")
                    print("El libro numero 5 ha sido prestado")
                    print(" al cliente con codigo:", (libre.get_codigo()))
                    print("desde hoy tiene 15 dias habiles para devolverlo")
                    print("en tal caso que no sea asi , usted sera betado")
                    print("muchas gracias")
                    print(".........................................")
                    libro_5.append(1)
                    self.__init__()
            
            if seleccion == 6:
                if 1 in libro_6:
                    print("ocupado o no existente")
                    self.__init__()
                else:
                    print(".........................................")
                    print("El libro numero 6 ha sido prestado")
                    print(" al cliente con codigo:", (libre.get_codigo()))
                    print("desde hoy tiene 15 dias habiles para devolverlo")
                    print("en tal caso que no sea asi , usted sera betado")
                    print("muchas gracias")
                    print(".........................................")
                    libro_6.append(1)
                    self.__init__()
                    
            if seleccion == 7:
                if 1 in libro_7:
                    print("ocupado o no existente")
                    self.__init__()
                else:
                    print(".........................................")
                    print("El libro numero 7 ha sido prestado")
                    print(" al cliente con codigo:", (libre.get_codigo()))
                    print("desde hoy tiene 15 dias habiles para devolverlo")
                    print("en tal caso que no sea asi , usted sera betado")
                    print("muchas gracias")
                    print(".........................................")
                    libro_7.append(1)
                    self.__init__()
        if seleccion == 8:
            print(".........................................")
            print(" ")
            exit()
libre = libroAprestar()