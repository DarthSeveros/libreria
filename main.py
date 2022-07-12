import movimiento
import producto
from getpass import getpass

import mysql.connector

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="libreria"
    )

    if mydb.is_connected():
        mycursor = mydb.cursor()
        userType = None   

        userName = input("Bienvenido, ingrese nombre de usuario: ")
        userPass = getpass("Ingrese contraseña: ")
        searchUserName = 'SELECT nombre_usuario, contrasena, tipo_usuario, id_usuario FROM usuario WHERE nombre_usuario = %s'
        mycursor.execute(searchUserName, [userName])
        userData = mycursor.fetchone()
        if (userData == None or userData[1] == userPass):
                print('El usuario o contraseña es incorrecto')
        else :
            userType = userData[2]
            idUsuario = userData[3]

        print("Bienvenido {}, ¿Qué desea hacer?".format(userName))
        
        if (userType == 'Jefe de bodega'):
            while(True):
                optionMainMenu = input('''
(1)Crear nueva bodega
(2)Eliminar bodega
(3)Ingresar producto nuevo
(4)Eliminar producto
(5)Asignar producto a una bodega
(6)Ingresar nuevo autor
(7)Eliminar autor
(8)Ingresar nueva editorial
(9)Eliminar editorial
(10)Salir\n''')
                if(optionMainMenu == '1'):
                    createBodega = 'INSERT INTO bodega () VALUES ();'
                    mycursor.execute(createBodega)
                    mydb.commit()

                elif(optionMainMenu == '2'):
                    idBodega = input('Ingrese el id de la bodega: ')
                    lookBodega = ('SELECT * FROM bodega')
                    i = mycursor.fetchone()
                    if (i != None):
                        print('La bodega no se encuentra vacía. Imposible elimninar')
                    else :
                        deleteBodega = 'DELETE FROM BODEGA WHERE id_bodega = {}'.format(idBodega)
                        mycursor.execute(deleteBodega)
                        mydb.commit()

                elif(optionMainMenu == '3'):
                    createProducto = 'INSERT INTO producto(titulo, tipo_producto, id_editorial, descripcion) VALUES(%s, %s, %s, %s)'
                    createRegistro = 'INSERT INTO registro(id_producto, id_autor) VALUES(%s, %s)'
                    numberTipoProducto = input('Seleccione el tipo de producto:\n(1)Libro\n(2)Revista\n(3)Enciclopedia\n')
                    titulo = input('Ingrese el nombre del producto: ')
                    while (numberTipoProducto != "1" and numberTipoProducto != "2" and numberTipoProducto != "3"):
                        print('Ingrese una entrada válida')
                        numberTipoProducto = input('Seleccione el tipo de producto:\n(1)Libro\n(2)Revista\n(3)Enciclopedia\n')
                        if (numberTipoProducto == "1"):
                            tipoProducto = "Libro"
                        elif (numberTipoProducto == "2"):
                            tipoProducto = "Revista"
                        else:
                            tipoProducto = "Eciclopedia"
                    if (numberTipoProducto == "1"):
                        tipoProducto = "Libro"
                    elif (numberTipoProducto == "2"):
                        tipoProducto = "Revista"
                    else:
                        tipoProducto = "Enciclopedia"
                    idEditorial = input('Ingrese id de la editorial: ')
                    descripcion = input('Ingrese descipcion: ')
                    mycursor.execute(createProducto, (titulo, tipoProducto, idEditorial, descripcion))
                    mydb.commit()
                    searchProducto = 'SELECT id_producto FROM producto WHERE titulo = %s AND idEditorial = %s'
                    mycursor.execute(searchProducto,(titulo, idEditorial))
                    idProducto = mycursor.fetchone()[0]
                    cantidadAutores = input('Ingrese la cantidad de autores: ')
                    for i in range(int(cantidadAutores)):
                        idAutor = input('Ingrese id del autor: ')
                        mycursor.execute(createRegistro, (idAutor, idProducto))
                
                elif (optionMainMenu == '4'):
                    deleteProducto = 'DELETE FROM producto WHERE id_producto = %s'
                    searchProducto = 'SELECT id_producto FROM lista_productos WHERE id_producto = %s'
                    idProducto = input('Ingrese id del producto: ')
                    mycursor.execute(searchProducto, [idProducto])
                    if ( mycursor.fetchone == None):
                        mycursor.execute(deleteProducto, [idProducto])
                        mydb.commit()
                    else:
                        print('El producto ya se encuentra asignado a una bodega, imposible eliminar')

                elif (optionMainMenu == '5'):
                    asignProducto = 'INSERT INTO lista_productos(id_bodega, id_producto, cantidad) VALUES (%s, %s, %s)'
                    idBodega = input('Ingrese el id de la bodega: ')
                    idProducto = input('Ingrese el id del producto: ')
                    cantidad = input('Ingrese la cantidad: ')
                    mycursor.execute(asignProducto,(idBodega, idProducto, cantidad))
                    mydb.commit()

                elif (optionMainMenu == '6'):
                    insertAutor = 'INSERT INTO autor (nombres, apellidos) VALUES(%s, %s)'
                    nombres = input('Ingrese los nombres del autor: ')
                    apellidos = input('Ingrese los apellidos del autor: ')
                    mycursor.execute(insertAutor,(nombres, apellidos))
                    mydb.commit()

                elif (optionMainMenu == '7'):
                    deleteAutor = 'DELETE FROM autor WHERE id_autor == %s'
                    searchAutor = 'SELECT id_autor FROM registro WHERE id_autor = %s'
                    idAutor = input('Ingrese el id del autor: ')
                    mycursor.execute(searchAutor, [idAutor])
                    if ( mycursor.fetchone == None):
                        mycursor.execute(deleteAutor, [idAutor])
                        mydb.commit()
                    else:
                        print('El autor ya se encuentra asignado a un producto. Imposible eliminar.')

                elif (optionMainMenu == '8'):
                    insertEditorial = 'INSERT INTO editorial (nombre_editorial) VALUES(%s)'
                    nombreEditorial = input('Ingrese el nombre de la editorial: ')
                    mycursor.execute(insertEditorial, [nombreEditorial])
                    mydb.commit()

                elif (optionMainMenu == '9'):
                    deleteEditorial = 'DELETE FROM editorial WHERE id_editorial == %s'
                    searchEditorial = 'SELECT id_editorial FROM producto WHERE id_editorial = %s'
                    nombreEditorial = input('Ingrese el nombre de la editorial: ')
                    mycursor.execute(searchEditorial, [idEditorial])
                    if ( mycursor.fetchone == None):
                        mycursor.execute(deleteEditorial, (nombreEditorial))
                        mydb.commit()
                    else:
                        print('La editorial ya se encuentra asignada a un producto. Imposible eliminar.')

                else:
                    print("Hasta pronto")
                    break
        
        elif (userType == 'Bodeguero'):
            while(True):
                optionMainMenu = input('''
(1)Mover productos
(2)Salir\n''')
                if (optionMainMenu == '1'):
                    insertListaProducto = 'INSERT INTO lista_productos (id_producto, id_bodega, cantidad) VALUES (%s, %s, %s)'
                    insertMovimiento = 'INSERT INTO movimiento (id_origen, id_destino, id_usuario) VALUES (%s, %s, %s)'
                    insertProductosMovimiento = 'INSERT INTO productos_movimiento (id_movimiento, id_producto, cantidad) VALUES (%s, %s, %s)'
                    searchListaProducto = 'SELECT cantidad FROM lista_productos WHERE id_bodega = %s AND id_producto = %s'
                    alterCantidadProducto = 'UPDATE lista_productos SET cantidad = %s WHERE id_bodega = %s AND id_producto = %s'

                    idBodegaOrigen = input('Ingrese la bodegan de origen: ')
                    idBodegaDestino = input('Ingrese la bodega de destino: ')
                    mycursor.execute(insertMovimiento, (idBodegaOrigen, idBodegaDestino, idUsuario))
                    mydb.commit()
                    movimientos = int(input('¿Cuantos productos distintos desea mover? '))
                    for i in range(movimientos):
                        idProducto = input('Ingrese id del producto: ')
                        mycursor.execute(searchListaProducto, (idBodegaOrigen, idProducto))
                        cantidadMovida = int(input('Ingrese la cantidad a mover: '))
                        cantidadTotal = int(mycursor.fetchone()[0]) - cantidadMovida
                        mycursor.execute(alterCantidadProducto, (cantidadMovida, idBodegaOrigen, idProducto))
                        mycursor.execute(searchListaProducto,(idBodegaDestino, idProducto))
                        
                        listaProducto = mycursor.fetchone()  
                        if (listaProducto == None):
                            mycursor.execute(insertListaProducto, (idProducto, idBodegaDestino, cantidadTotal))
                        else:
                            cantidadTotal = cantidadMovida + int(listaProducto[0])
                            mycursor.execute(alterCantidadProducto,(cantidadTotal, idBodegaDestino, idProducto))
                    mydb.commit()
                else:
                    print("Hasta pronto")
                    break
finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print('Conexión finalizada')