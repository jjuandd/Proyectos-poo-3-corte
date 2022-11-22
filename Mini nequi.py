ListaContraseñas = []
Cuenta_Corriente = []
Cuenta_de_Ahorro = []    
Lista_de_los_Usuarios = []        
class Registrar:
    def registro(self):
        self.cliente = input("nombre:  ")
        if self.cliente in (Lista_de_los_Usuarios):
            print("======================")
            print("Usuario no encontrado ")
            print("======================")
            self.registro()
        else:
            self.clave = int(input("clave:  "))
            Lista_de_los_Usuarios.append(self.cliente)
            ListaContraseñas.append(self.clave)
            self.__init__()
class registro_de_nuevo_usuario():
    def registro_de_nuevo_usuario(self):
        cliente = input("Digite su usuario por favor:  ")
        if cliente in Lista_de_los_Usuarios:
            print("===============")
            clave = int(input("ingresa la contraseña por favor: "))
            if clave in ListaContraseñas:
                print("================")
                print("registro añadido ")
                print("================")
            else:
                print("Contraseña Incorrecta ")
                self.registro_de_nuevo_usuario()
        else:
            print("================================")
            print("ERROR")
            print("el nombre de usuario no existe ")
            print("================================")
            exit()
class comienzo(Registrar,registro_de_nuevo_usuario):
    def __init__(self):
        print("1 => iniciar sesion ")
        print("2 => Registro de usuarios")
        eleccion = int(input("selecciona la opcion deseada "))
        if eleccion == 1:
            super(comienzo,self).registro_de_nuevo_usuario()
        if eleccion == 2:
            super(comienzo,self).registro()
class diego(comienzo):
    def __init__(self):
        super().__init__()
        self.list()
    def list(self):
        print("1 => Administracion de tu cuenta")
        print("2 => cerrar cuenta ")
        eleccion = int(input("ingrese la opcion deseada "))
        if eleccion == 1:
            self.vercuenta()
        if eleccion == 2:
            self.__init__()
            Cuenta_de_Ahorro.clear()
            Cuenta_Corriente.clear()
    def opcioncuentas(self):
        print("1 => Cuenta corriente  ")
        print("2 => Cuenta de ahorros ")
        eleccion = int(input("elija el tipo de cuenta"))
        if eleccion == 1:
            saldo = float(input("ingrese el monto a depositar  "))
            Cuenta_Corriente.append(saldo)
            print("Depositado con exito ")
            self.list()
        elif eleccion == 2:
            saldo = float(input("ingrese el monto a depositar"))
            Cuenta_de_Ahorro.append(saldo)
            print("Depositado con exito  ")
            self.list()
        else:
            print("error  ")
            self.list()
    def elegircuenta(self):
        print("1 => Cuenta corriente  ")
        print("2 => Cuenta de ahorros  ")
        eleccion = int(input("Digite una opcion  "))
        if eleccion == 1:
            print("El monto seria de: $ ",sum(Cuenta_Corriente))
        elif eleccion == 2:
            print("El monto seria de : $ ",sum(Cuenta_de_Ahorro))
        else:
            print("Error ")
            self.list
    def vercuenta(self):
        print("1 => Depositar dinero ")
        print("2 => Retirar saldo")
        print("3 => salir de la cuenta")
        eleccion = int(input("Digite su desicion  "))
        if eleccion == 1:
            print("1 => Cuenta corriente  ")
            print("2 => Cuenta de ahorros  ")
            eleccion = int(input("Seleccione el tipo de cuenta  "))
            if eleccion == 1:
                saldo = float(input("ingrese el valor:  "))
                Cuenta_Corriente.append(saldo)
                self.list()
            elif eleccion == 2:
                saldo = float(input("ingrese el valor "))
                Cuenta_de_Ahorro.append(saldo)
                self.list()
            else:
                print("===================")
                print("Error ")
                print("===================")
                self.list()
        if eleccion == 2:
            Total_de_la_Cuenta_de_Ahorro = sum(Cuenta_de_Ahorro)
            Total_de_la_Cuenta_Corriente = sum(Cuenta_Corriente)
            print("1 => Cuenta corriente  ")
            print("2 => Cuenta de ahorro ")
            seleccion = int(input("seleccione el tipo de cuenta "))
            if seleccion == 2:
                print("Saldo actual : ",Cuenta_de_Ahorro)
                dineroRetirado = int(input("Digite la cantidad de dinero a retirar: "))
                if dineroRetirado < Total_de_la_Cuenta_de_Ahorro:
                    Dineroquequedo =  Total_de_la_Cuenta_de_Ahorro - dineroRetirado
                    Cuenta_de_Ahorro.clear()
                    Cuenta_de_Ahorro.append(Dineroquequedo)
                    print("Su nuevo saldo es de : ", Cuenta_de_Ahorro)
                    self.list()
                if dineroRetirado > Total_de_la_Cuenta_de_Ahorro:
                    print("===================")
                    print("error  ")
                    print("saldo insuficiente  ")
                    print("===================")
                    self.list()
            if seleccion == 1:
                print("Saldo actual : ",Cuenta_Corriente)
                dineroRetirado = int(input("Digite la cantidad de dinero a retirar  "))
                if dineroRetirado < Total_de_la_Cuenta_Corriente:
                    Dineroquequedo = Total_de_la_Cuenta_Corriente - dineroRetirado 
                    Cuenta_Corriente.clear()
                    Cuenta_Corriente.append(Dineroquequedo)
                    print("Su nuevo saldo: ", Cuenta_Corriente)
                    self.list()
                if dineroRetirado > Total_de_la_Cuenta_Corriente:
                    print("===================")
                    print("Error. ")
                    print("Dinero insuficiente ")
                    print("===================")
                    self.list()             
        if eleccion == 3:
            exit()
diego()
registro_de_nuevo_usuario()
comienzo()