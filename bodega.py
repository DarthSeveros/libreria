
class bodega:
    def __init__(self, id):
        self.__id = id
        self.__productos = []

    def dropProducto(self, titulo):
        for producto in self.__productos:
            if producto.getTitulo() == titulo:
                self.__productos.remove(producto)
    
    def addProducto(self, producto):
        self.__productos.append(producto)

    def getId(self):
        return self.__id
    
    def getProductos(self):
        return self.__productos