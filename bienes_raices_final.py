casas=[]
class Cuarto:
    """
    ventanas
    medida
    """    
    def __init__(self,ventanas,medida):
        self.__ventanas=ventanas
        self.__medida=medida

    def getVentanas(self):
        return self.__ventanas
    def setVentanas(self,valor):
        self.__ventanas=valor
    def getMedidas(self):
        return self.__medida
    def setMedidas(self,valor):
        self.__medidas=valor
        
    def __str__(self):
        return f"cuenta con {self.__ventanas} ventanas y mide {self.__medida}."
class Sala:
    """
    chimenea=booleano
    descripcion
    """    
    def __init__(self,chimenea,descripcion,):
        self.__chimena=chimenea
        self.__descripcion=descripcion

    def getChimenea(self):
        return self.__chimena
    def setChimenea(self,valor):
        self.__chimenea=valor
    def getDescripcion(self):
        return self.__descripcion
    def setDescripcion(self,valor):
        self.__descripcion=valor
    def __str__(self):
        if self.__chimena:
            chimenea="con chimenea"
        else:
            chimenea="sin chimenea"
        return f"descripcion de la sala: {self.__descripcion}, {chimenea}."
        
class Lavatrastes:
    """
    depositos
    agua=booleano
    """    
    def __init__(self,depositos,agua):
        self.__depositos=depositos
        self.__agua=agua
    
    def getDepositos(self):
        return self.__depositos
    def setDepositos(self,valor):
        self.__depositos=valor

    def getAgua(self):
        return self.__agua
    def setAgua(self,valor):
        self.__agua=valor

    def __str__(self):
        agua = "con agua caliente" if self.__agua else "sin agua caliente"
        return f"Lavatrastes con {self.__depositos} huecos y {agua}."
    
class Cocina:
    """
    descripcion
    electrodomesticos
    medidas
    material
    lavatrastes=objeto
    """    
    def __init__(self,descripcion,electrodomesticos,medidas,material,lavatrastes):
        self.__descripcion=descripcion
        self.__electrodomesticos=electrodomesticos
        self.__medidas=medidas
        self.__material=material
        self.lavatrastes=lavatrastes
    
    def getDescripcion(self):
        return self.__descripcion    
    def setDescripcion(self,valor):
        self.__descripcion=valor
    def getElectrodomesticos(self):
        return self.__electrodomesticos
    def setElectrodomesticos(self,valor):
        self.__electrodomesticos=valor
    def getMedidas(self):
        return self.__medidas
    def setMedidas(self,valor):
        self.__medidas=valor
    def getMaterial(self):
        return self.__material
    def setMaterial(self,valor):
        self.__material=valor
    def __str__(self):
        electricos = "con electrodomesticos" if self.getElectrodomesticos() else "sin electrodomesticos"
        return f"descripción: {self.__descripcion}, cuenta con {self.__medidas}, {electricos}, el material del comedor es {self.__material}, {self.lavatrastes}"

class Patio:
    """
    medidas
    areasocial
    descripcion
    """    
    def __init__(self,medidas,areaSocial,descripcion):
        
        self.__medidas=medidas
        self.__areaSocial=areaSocial
        self.__descripcion=descripcion
    
    def getMedidas(self):
        return self.__medidas
    def setMedidas(self,valor):
        self.__medidas=valor
    def getAreaSocial(self):
        return self.__areaSocial
    def setAreaSocial(self,valor):
        self.__areaSocial=valor
    def getDescripcion(self):
        return self.__descripcion
    def setDescripcion(self,valor):
        self.__descripcion=valor
    def __str__(self):
        areasocial = "con área social" if self.getAreaSocial() else "sin área social"
        return f"descripción: {self.__descripcion}, {areasocial}, cuenta con medidas de {self.__medidas}."
    
class Estado:
    """
    estado
    fecha
    """    
    def __init__(self,estado, fecha):
        self.__estado=estado
        self.__fecha=fecha
    
    def getEstado(self):
        return self.__estado
    def setEstado(self,valor):
        self.__estado=valor
    def getFecha(self):
        return self.__fecha
    def setFecha(self, valor):
        self.__fecha=valor
    def __str__(self):
        return f"El estado de la casa es {self.__estado} desde {self.__fecha}"
    
class Casa:
    """
    direccion
    cuartos[]
    salas[]
    cocinas[]
    patios[]
    estados[]
    """    
    def __init__(self,direccion,):
        self.__direccion=direccion
        self.__cuartos=[]
        self.__salas=[]
        self.__cocinas=[]
        self.__patios=[]
        self.__estados=[]
    def agregarCuarto(self,cuarto):
        self.__cuartos.append(cuarto)
    def agregarSala(self,sala):
        self.__salas.append(sala)
    def agregarCocina(self,cocina):
        self.__cocinas.append(cocina)
    def agregarPatio(self,patio):
        self.__patios.append(patio)
    def agregarEstado(self,estado):
        self.__estados.append(estado)
    def getCuartos(self):
        for i,cuarto in enumerate (self.__cuartos, start=1):
            return cuarto
    def getCocinas(self):
        for i,cocina in enumerate (self.__cocinas, start=1):
            return cocina
    def getPatios(self):
        for i,patio in enumerate (self.__patios, start=1):
            return patio
    def getEstados(self):
        for i,estado in enumerate (self.__estados, start=1):
            return estado
    def getSalas(self):
        for i,sala in enumerate (self.__salas, start=1):
            return sala
    def __str__(self):
        return f"Casa con direccion {self.__direccion}\n*salas:   {self.getSalas()}\n*cuartos: {self.getCuartos()}\n*cocinas: {self.getCocinas()}\n*patios:  {self.getPatios()}\n*estados: {self.getEstados()}"

def Menu():
    casas = []
    while True:
        print("\n1. Agregar Casa")
        print("2. Mostrar Casas")
        print("3. Modificar Casa")
        print("4. Eliminar Casa")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            direccion = input("Ingrese la dirección de la casa: ")
            casa = Casa(direccion)
            while True:
                print("\nAgregar:")
                print("1. Cuarto")
                print("2. Sala")
                print("3. Cocina")
                print("4. Patio")
                print("5. Estado")
                print("6. Terminar de agregar")
                opcion_agregar = input("Seleccione una opción para agregar a la casa: ")
                if opcion_agregar == "1":
                    ventanas = input("Ingrese el número de ventanas del cuarto: ")
                    medida = input("Ingrese la medida del cuarto: ")
                    cuarto = Cuarto(ventanas, medida)
                    casa.agregarCuarto(cuarto)
                    
                    print("Cuarto agregado correctamente.")
                elif opcion_agregar == "2":
                    chimenea = input("¿La sala cuenta con chimenea?1. si, 2. no ")
                    booleano=False
                    if chimenea==1:
                        booleano=True
                    elif chimenea==2:
                        booleano=False
                    descripcion = input("Ingrese una descripción de la sala: ")
                    sala = Sala(booleano, descripcion)
                    casa.agregarSala(sala)                    
                    print("Sala agregada correctamente.")
                elif opcion_agregar == "3":
                    descripcion = input("Ingrese una descripción de la cocina: ")
                    electrodomesticos = input("¿La cocina cuenta con electrodomésticos? 1. si, 2. no ")
                    booleano1=False
                    booleano2=False
                    if electrodomesticos==1:
                        booleano1=True
                    elif electrodomesticos==2:
                        booleano1=False
                    medidas = input("Ingrese las medidas de la cocina: ")
                    material = input("Ingrese el material del comedor: ")
                    lavatrastes_depositos = input("Ingrese el número de depósitos del lavatrastes: ")
                    lavatrastes_agua = int(input("¿El lavatrastes cuenta con agua caliente? 1. si, 2. no "))
                    if lavatrastes_agua==1:
                        booleano2=True
                    elif lavatrastes_agua==2:
                        booleano2=False
                    lavatrastes = Lavatrastes(lavatrastes_depositos, booleano2)
                    cocina = Cocina(descripcion, booleano1, medidas, material, lavatrastes)
                    casa.agregarCocina(cocina)
                    print("Cocina agregada correctamente.")
                elif opcion_agregar == "4":
                    medidas = input("Ingrese las medidas del patio: ")
                    areaSocial = int(input("¿El patio cuenta con área social? 1. si, 2. no "))
                    booleano=False
                    if areaSocial==1:
                        booleano=True
                    elif areaSocial==2:
                        booleano=False
                    descripcion = input("Ingrese una descripción del patio: ")
                    patio = Patio(medidas, booleano, descripcion)
                    casa.agregarPatio(patio)                    
                    print("Patio agregado correctamente.")
                elif opcion_agregar == "5":
                    estado = input("Ingrese el estado de la casa: ")
                    fecha = input("Ingrese la fecha del estado: ")
                    estadoobjeto = Estado(estado, fecha)
                    casa.agregarEstado(estadoobjeto)                                        
                    print("Estado agregado correctamente.")
                elif opcion_agregar == "6":
                    casas.append(casa)
                    print("Casa agregada correctamente.")
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
        elif opcion == "2":
            for i,casa in enumerate(casas, start=1):
                print(f"*casa: {i}  {casa}\n")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
Menu()