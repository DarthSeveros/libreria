CREATE DATABASE libreria;
USE libreria;

CREATE TABLE usuario(
id_usuario INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
nombre_usuario varchar(20) NOT NULL, 
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
tipo_producto VARCHAR(12) NOT NULL,
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
id_bodega INT PRIMARY KEY NOT NULL AUTO_INCREMENT
);

CREATE TABLE movimiento(
id_movimiento INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
id_origen INT NOT NULL,
id_destino INT NOT NULL,
id_usuario INT NOT NULL,
fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (id_origen) REFERENCES bodega(id_bodega),
FOREIGN KEY (id_destino) REFERENCES bodega(id_bodega),
FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

CREATE TABLE lista_productos(
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
id_producto INT NOT NULL,
id_bodega INT NOT NULL,
cantidad INT NOT NULL,
FOREIGN KEY (id_bodega) REFERENCES bodega(id_bodega),
FOREIGN KEY (id_producto) REFERENCES producto(id_producto)
);

CREATE TABLE productos_movimiento(
id_productos_movimiento INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
id_movimiento INT NOT NULL,
id_producto INT NOT NULL,
cantidad INT NOT NULL,
FOREIGN KEY (id_movimiento) REFERENCES movimiento(id_movimiento),
FOREIGN KEY (id_producto) REFERENCES producto(id_producto)
);

INSERT INTO usuario (nombre_usuario, tipo_usuario, contrasena) VALUES ('joseivecas', 'Jefe de bodega', 'abc123');
INSERT INTO usuario (nombre_usuario, tipo_usuario, contrasena) VALUES ('taly', 'Bodeguero', '123abc');