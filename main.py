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

            else:
                print("Hasta pronto")
                break
finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print('Conexión finalizada')