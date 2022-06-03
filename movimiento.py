class movimiento:
    def __init__(self, origen, destino, productos, usuario):
        self.__origen = origen
        self.__destino = destino
        self.__productos = productos
        self.__usuario = usuario

    def generarPreviaDocumentoMovimiento(self):
        return [self.__origen, self.__destino, self.__productos, self.__usuario]
    
    def generarDocumentoMovimiento(self):
        return[self.__origen, self.__destino, self.__productos]
    