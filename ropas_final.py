class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad

    def mostrar_info(self):
        pass

    #Encapsulamiento de nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getNombre(self):
        return self.__nombre
    
    #Encapsulamiento de precio
    def setPrecio(self, precio):
        self.__precio = precio
    
    def getPrecio(self):
        return self.__precio
    
    #Encapsulamiento de cantidad
    def setCantidad(self, cantidad):
        self.__cantidad = cantidad
    
    def getCantidad(self):
        return self.__cantidad
        
#Aplicando polimorfismo  
class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.__talla = talla

    def mostrar_info(self):
        print(f"{self.getNombre()}      {self.getPrecio()}       {self.getCantidad()}        {self.getTalla()}")  
    
    #Encapsulamiento de talla
    def setTalla(self, talla):
        self.__talla = talla
    
    def getTalla(self):
        return self.__talla
    
#Aplicando polimorfismo
class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.__talla = talla

    def mostrar_info(self):        
        print(f"{self.getNombre()}      {self.getPrecio()}       {self.getCantidad()}        {self.getTalla()}")       
    
    #Encapsulamiento de talla
    def setTalla(self, talla):
        self.__talla = talla
    
    def getTalla(self):
        return self.__talla

#Abstraccion
class Inventario():
    def __init__(self):
        #Lista de prendas
        self.prendas = []
    
    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)

    def eliminar_prenda(self, prenda):
        self.prendas.remove(prenda)
    
    def mostrar_inventario(self):
        for prenda in self.prendas:
            prenda.mostrar_info()

#IMPLEMENTACION DEL EJERCICIO
#Instancias Ropa de hombre y de mujer
camisa = RopaHombre("Camisa masculina", 25000, 50, "M")
falda = RopaMujer("Falda para mujer", 85000, 15, "P")
pantalon = RopaHombre("Pantalon de vestir Negro", 105000, 45, "XL")
falda = RopaMujer("Blusa mini", 40000, 35, "S")
short = RopaHombre("Short sport gris", 70000, 115, "G")

#Crear inventario
inventario = Inventario()

inventario.agregar_prenda(camisa)
inventario.agregar_prenda(falda)
inventario.agregar_prenda(pantalon)
inventario.agregar_prenda(falda)
inventario.agregar_prenda(short)

#Listar Prendas
inventario.mostrar_inventario()