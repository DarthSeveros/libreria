class produto:
    def __init__(self, titulo, tipo, editorial, autores, descripcion):
        self.__titulo = titulo
        self.__tipo = tipo
        self.__editorial = editorial
        self.__autores = autores
        self.__descripcion = descripcion

    def getTitulo(self):
        return self.__titulo

    def getTipo(self):
        return self.__tipo

    def getEditorial(self):
        return self.__editorial

    def getAutores(self):
        return self.__autores

    def getDescripcion(self):
        return self.__descripcion

    


    
