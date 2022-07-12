import movimiento
import producto

import mysql.connector
from mysql.connector.errors import Error

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="libreria"
    )

    if mydb.is_connected():
        mycursor = mydb.cursor()
        insertAutor = 'INSERT INTO autor(nombres, apellidos) VALUES(%s, %s)'      

        print("Bienvenido, ¿Qué desea hacer?")
        
        while(True):
            optionMainMenu = input('''
(1)Crear nueva bodega
(2)Eliminar bodega
(3)Ingresar producto nuevo
(4)Eliminar producto
(5)Asignar producto a una bodega
(6)Mover productos
(7)Ingresar nuevo autor
(8)Eliminar autor
(9)Ingresar nueva editorial
(10)Eliminar editorial
(11)Salir\n''')
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
                    tipoProducto = "Eciclopedia"
                idEditorial = input('Ingrese id de la editorial: ')
                descripcion = input('Ingrese descipcion: ')
                mycursor.execute(createProducto, (titulo, tipoProducto, idEditorial, descripcion))
                mydb.commit()
            
            elif (optionMainMenu == '4'):
                deleteProducto = 'DELETE FROM producto WHERE id_producto = %s'
                idProducto = input('Ingrese id del producto: ')
                mycursor.execute(deleteProducto, idProducto)
                mydb.commit()

            elif (optionMainMenu == '5'):
                asignProducto = 'INSERT INTO lista_productos(id_bodega, id_producto, cantidad) VALUES (%s, %s, %s)'
                idBodega = input('Ingrese el id de la bodega: ')
                idProducto = input('Ingrese el id del producto: ')
                cantidad = input('Ingrese la cantidad: ')
                mycursor.execute(asignProducto,(idBodega, idProducto, cantidad))
                mydb.commit()

            elif (optionMainMenu == '6'):
                moveProducto = 'UPDATE lista_productos SET id_bodega = %s WHERE id_bodega = %s AND id_producto = %s'
                idProducto = input('Ingrese id del producto: ')
                idBodegaOrigen = input('Ingrese la bodegan de origen: ')
                idBodegaDdestino = input('Ingrese la bodega de destino: ')
                mycursor.execute(moveProducto, (idBodegaDdestino, idBodegaOrigen, idProducto))

            elif (optionMainMenu == '7'):
                insertAutor = 'INSERT INTO autor (nombres, apellidos) VALUES(%s, %s)'
                nombres = input('Ingrese los nombres del autor: ')
                apellidos = input('Ingrese los apellidos del autor: ')
                mycursor.execute(insertAutor,(nombres, apellidos))
                mydb.commit()

            elif (optionMainMenu == '8'):
                deleteAutor = 'DELETE FROM autor WHERE id_autor == %s'
                idAutor = input('Ingrese el id del autor: ')
                mycursor.execute(deleteAutor, (idAutor))
                mydb.commit()

            elif (optionMainMenu == '9'):
                insertEditorial = 'INSERT INTO editorial (nombre_editorial) VALUES(%s)'
                nombreEditorial = input('Ingrese el nombre de la editorial: ')
                mycursor.execute(insertEditorial, [nombreEditorial])
                mydb.commit()

            elif (optionMainMenu == '10'):
                deleteEditorial = 'DELETE FROM editorial WHERE id_editorial == %s'
                nombreEditorial = input('Ingrese el nombre de la editorial: ')
                mycursor.execute(deleteAutor, (nombreEditorial))
                mydb.commit()

            else:
                print("Hasta pronto")
                break
finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print('Conexión finalizada')