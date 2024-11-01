# Clase base para los productos
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_informacion(self):
        # Método para mostrar la información del producto
        print(f"Producto: {self.nombre}, Precio: {self.precio}")

# Clases específicas para cada tipo de producto
class Camisa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

class Pantalon(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

class Zapato(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

# Clase para gestionar la tienda
class Tienda:
    def __init__(self):
        self.productos = []
        self.carrito = []  # Carrito de compras

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos disponibles.")
        else:
            for i, producto in enumerate(self.productos):  
                print(f"{i + 1}. {producto.nombre} - {producto.precio}")

    def seleccionar_producto(self, indice):
        
        producto = self.productos[indice - 1]
        self.carrito.append(producto)
        print(f"Se ha añadido {producto.nombre} al carrito.")

    def mostrar_carrito(self):
        print("Carrito de compras:")
        total = 0
        for producto in self.carrito:
            producto.mostrar_informacion()
            total += producto.precio
        print(f"Total: {total}")  

    def procesar_compra(self):
        print("Procesando compra...")
        self.carrito.clear()  
        print("Compra realizada con éxito.")

# Ejemplo de uso del sistema
def main():
    tienda = Tienda()
    
    # Agregar productos a la tienda
    tienda.agregar_producto(Camisa("Camisa Casual", 19.99, "M"))
    tienda.agregar_producto(Pantalon("Pantalón Jeans", 29.99, 32))
    tienda.agregar_producto(Zapato("Zapato Deportivo", 49.99, 42))

    while True:
        print("\n--- Menú de la Tienda ---")
        print("1: Ver productos")
        print("2: Seleccionar producto")
        print("3: Ver carrito")
        print("4: Procesar compra")
        print("5: Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            tienda.mostrar_productos()
        elif opcion == '2':
            tienda.mostrar_productos()
            try:
                indice = int(input("Seleccione el número del producto: ")) 
                tienda.seleccionar_producto(indice)
            except (ValueError, IndexError):
                print("Selección no válida.")
        elif opcion == '3':
            tienda.mostrar_carrito()
        elif opcion == '4':
            tienda.procesar_compra()
        elif opcion == '5':
            print("Gracias por su visita.")
            break
        else:
            print("Opción no válida.")  

# Ejecutar el programa principal
main()
