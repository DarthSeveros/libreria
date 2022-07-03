CREATE DATABASE libreria;
USE libreria;

CREATE TABLE usuario(
id_usuario INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
tipo_usuario VARCHAR(14) NOT NULL,
contrasena VARCHAR(15) NOT NULL
);

CREATE TABLE editorial(
id_editorial INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nombre_editorial VARCHAR(50) NOT NULL
);


CREATE TABLE autor(
id_autor INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
nombres VARCHAR(40) NOT NULL,
apellidos VARCHAR(40) NOT NULL
);

CREATE TABLE producto(
id_producto INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
titulo VARCHAR(50) NOT NULL,
id_editorial INT NOT NULL,
descripcion VARCHAR(100),
cantidad INT NOT NULL,
FOREIGN KEY (id_editorial) REFERENCES libreria.editorial(id_editorial)
);

CREATE TABLE registro(
id_registro INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
id_producto INT NOT NULL,
id_autor INT NOT NULL,
FOREIGN KEY(id_producto) REFERENCES libreria.producto(id_producto),
FOREIGN KEY(id_autor) REFERENCES libreria.autor(id_autor)
);

CREATE TABLE bodega(
id_bodega INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
id_producto INT NOT NULL,
FOREIGN KEY(id_producto) REFERENCES libreria.producto(id_producto)
);

