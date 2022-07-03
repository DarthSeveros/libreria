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
tipo_producto VARCHAR(12) NOT NULL,
id_editorial INT NOT NULL,
descripcion VARCHAR(100),
cantidad INT NOT NULL,
FOREIGN KEY (id_editorial) REFERENCES libreria.editorial(id_editorial)
);

ALTER TABLE producto ADD COLUMN (tipo_producto VARCHAR(12) NOT NULL);

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

drop table movimiento;
drop table bodega;
drop table lista_productos;
alter table producto drop column cantidad;

CREATE TABLE lista_productos(
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
id_producto INT NOT NULL,
id_bodega INT NOT NULL,
cantidad INT NOT NULL,
FOREIGN KEY (id_bodega) REFERENCES bodega(id_bodega),
FOREIGN KEY (id_producto) REFERENCES producto(id_producto)
);

INSERT INTO editorial (nombre_editorial) VALUES("Abraxas");
INSERT INTO editorial (nombre_editorial) VALUES("Acantilado");
INSERT INTO editorial (nombre_editorial) VALUES("Adn Editores");
INSERT INTO editorial (nombre_editorial) VALUES("Alfaguara");
INSERT INTO editorial (nombre_editorial) VALUES("Biblok");
INSERT INTO editorial (nombre_editorial) VALUES("Catedra");
INSERT INTO editorial (nombre_editorial) VALUES("Catalonia");
INSERT INTO editorial (nombre_editorial) VALUES("Debate");
INSERT INTO editorial (nombre_editorial) VALUES("Debolsillo");

show tables;

INSERT INTO bodega () VALUES ();
select * from editorial;

SELECT producto.tipo_producto,
producto.titulo,
editorial.nombre_editorial,
producto.cantidad
FROM producto, editorial WHERE 
producto.id_editorial = editorial.id_editorial;

SELECT id_producto FROM producto WHERE titulo = 'La invasion'; 

ALTER TABLE bodega AUTO_INCREMENT = 1;
DELETE FROM bodega; 

INSERT INTO producto(titulo, tipo_producto, id_editorial, descripcion, cantidad) VALUES("La montaña mágica", "Libro", 7, "sanatorio", 1);