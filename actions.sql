use libreria;

drop table movimiento;
drop table bodega;
drop table lista_productos;
drop table producto;
drop table registro;
alter table producto drop column cantidad;

INSERT INTO editorial (nombre_editorial) VALUES("Abraxas");
INSERT INTO editorial (nombre_editorial) VALUES("Acantilado");
INSERT INTO editorial (nombre_editorial) VALUES("Adn Editores");
INSERT INTO editorial (nombre_editorial) VALUES("Alfaguara");
INSERT INTO editorial (nombre_editorial) VALUES("Biblok");
INSERT INTO editorial (nombre_editorial) VALUES("Catedra");
INSERT INTO editorial (nombre_editorial) VALUES("Catalonia");
INSERT INTO editorial (nombre_editorial) VALUES("Debate");
INSERT INTO editorial (nombre_editorial) VALUES("Debolsillo");

INSERT INTO usuario (nombre_usuario, tipo_usuario, contrasena) VALUES ('joseivecas', 'Jefe de bodega', 'abc123');
INSERT INTO usuario (nombre_usuario, tipo_usuario, contrasena) VALUES ('taly', 'Bodeguero', '123abc');
commit;

INSERT INTO `registro` (`id_producto`, `id_autor`) VALUES ('1', '1');

show tables;
SELECT * FROM bodega;
SELECT * FROM lista_productos;
SELECT * FROM producto;

INSERT INTO bodega () VALUES ();
select * from editorial;

SELECT lista_productos.id,
producto.titulo,
bodega.id_bodega
FROM lista_productos, producto, bodega
WHERE
lista_productos.id_bodega = bodega.id_bodega and
lista_productos.id_producto = producto.id_producto;

SELECT producto.tipo_producto,
producto.titulo,
editorial.nombre_editorial,
producto.cantidad
FROM producto, editorial WHERE 
producto.id_editorial = editorial.id_editorial;

SELECT id_producto FROM producto WHERE titulo = 'La invasion'; 

ALTER TABLE bodega AUTO_INCREMENT = 1;
ALTER TABLE producto AUTO_INCREMENT = 1;
ALTER TABLE usuario ADD COLUMN nombre_usuario varchar(20) NOT NULL;
DELETE FROM bodega;
DELETE FROM producto WHERE id_producto = 6; 

INSERT INTO producto(titulo, tipo_producto, id_editorial, descripcion, cantidad) VALUES("La montaña mágica", "Libro", 7, "sanatorio", 1);

SELECT bodega.id_bodega, 
lista_productos.id_producto,
lista_productos.cantidad FROM 
bodega LEFT JOIN lista_productos
ON bodega.id_bodega = lista_productos.id_bodega;

SELECT * FROM registro WHERE id_autor = '2';
SELECT cantidad FROM lista_productos WHERE id_bodega = 1 AND id_producto = 1;

SELECT id_movimiento FROM movimiento ORDER BY id_movimiento DESC LIMIT 1;


