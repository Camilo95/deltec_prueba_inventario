-- --------------------------------------------------------
-- Host:                         C:\users\camiloobando\Mis Documentos\PAGINAS WEB\deltec\gestion_inventario\db.sqlite3
-- Versión del servidor:         3.34.0
-- SO del servidor:              
-- HeidiSQL Versión:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES  */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando estructura para tabla db.inventario_asignado
CREATE TABLE IF NOT EXISTS "inventario_asignado" ("id" char(32) NOT NULL PRIMARY KEY, "fecha_asignacion" datetime NOT NULL, "fecha_desvinculacion" datetime NULL, "persona_id" char(32) NOT NULL REFERENCES "inventario_persona" ("id") DEFERRABLE INITIALLY DEFERRED, "recurso_id" char(32) NOT NULL REFERENCES "inventario_recurso" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Volcando datos para la tabla db.inventario_asignado: -1 rows
/*!40000 ALTER TABLE "inventario_asignado" DISABLE KEYS */;
INSERT INTO "inventario_asignado" ("id", "fecha_asignacion", "fecha_desvinculacion", "persona_id", "recurso_id") VALUES
	('bc672b03dd244897b85a8cd8093712dc', '2021-11-05 20:30:25.106502', NULL, 'f3b31ef12c284979a7fd2a04d9301d37', 'c11143032a924176b66c372b836d435a');
/*!40000 ALTER TABLE "inventario_asignado" ENABLE KEYS */;

-- Volcando estructura para tabla db.inventario_categoria
CREATE TABLE IF NOT EXISTS "inventario_categoria" ("id" char(32) NOT NULL PRIMARY KEY, "nombre" varchar(500) NOT NULL UNIQUE);

-- Volcando datos para la tabla db.inventario_categoria: -1 rows
/*!40000 ALTER TABLE "inventario_categoria" DISABLE KEYS */;
INSERT INTO "inventario_categoria" ("id", "nombre") VALUES
	('dfae0611ac9d4c338471fc585072e35b', 'Perifericos'),
	('79ca19a5e3dc45e3a93951323aa2dfd5', 'Celular'),
	('7d28aa7da389413cbc43300c8127e61c', 'Monitor'),
	('d5903dcd904f4e0bb9fbdf0693b72a58', 'Tablet');
/*!40000 ALTER TABLE "inventario_categoria" ENABLE KEYS */;

-- Volcando estructura para tabla db.inventario_marca
CREATE TABLE IF NOT EXISTS "inventario_marca" ("id" char(32) NOT NULL PRIMARY KEY, "nombre" varchar(500) NOT NULL UNIQUE);

-- Volcando datos para la tabla db.inventario_marca: -1 rows
/*!40000 ALTER TABLE "inventario_marca" DISABLE KEYS */;
INSERT INTO "inventario_marca" ("id", "nombre") VALUES
	('c1adf01f822443fcb8c093c622614f59', 'Dell'),
	('08ac3d59cd17426ca9b2fe90ac33ba4b', 'HP'),
	('9c769abb7e88459f8342307bbfcfb599', 'Genius'),
	('a70f6ecc7f2c44138283bf5520363fd2', 'Logitech'),
	('c0f31451e58c4b78a133b20349aa66d5', 'Asus'),
	('532c9137d5174d37ad29a8853fb35e08', 'Huawei'),
	('c3dd8db84b5b4e64929c2f91a2efaf0e', 'Xiaomi'),
	('2d8a8ed8b71b4fe78b45a15c4d2e17eb', 'Apple'),
	('dc006d12131c449695eb4f2d24eb2e7d', 'Acer');
/*!40000 ALTER TABLE "inventario_marca" ENABLE KEYS */;

-- Volcando estructura para tabla db.inventario_persona
CREATE TABLE IF NOT EXISTS "inventario_persona" ("id" char(32) NOT NULL PRIMARY KEY, "identificacion" varchar(20) NOT NULL UNIQUE, "nombres" varchar(400) NOT NULL, "apellidos" varchar(400) NOT NULL);

-- Volcando datos para la tabla db.inventario_persona: -1 rows
/*!40000 ALTER TABLE "inventario_persona" DISABLE KEYS */;
INSERT INTO "inventario_persona" ("id", "identificacion", "nombres", "apellidos") VALUES
	('f3b31ef12c284979a7fd2a04d9301d37', '1113677409', 'Camilo', 'Obando');
/*!40000 ALTER TABLE "inventario_persona" ENABLE KEYS */;

-- Volcando estructura para tabla db.inventario_recurso
CREATE TABLE IF NOT EXISTS "inventario_recurso" ("id" char(32) NOT NULL PRIMARY KEY, "codigo" varchar(50) NOT NULL UNIQUE, "nombre" varchar(1000) NOT NULL, "serial" varchar(100) NOT NULL, "categoria_id" char(32) NOT NULL REFERENCES "inventario_categoria" ("id") DEFERRABLE INITIALLY DEFERRED, "marca_id" char(32) NOT NULL REFERENCES "inventario_marca" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Volcando datos para la tabla db.inventario_recurso: -1 rows
/*!40000 ALTER TABLE "inventario_recurso" DISABLE KEYS */;
INSERT INTO "inventario_recurso" ("id", "codigo", "nombre", "serial", "categoria_id", "marca_id") VALUES
	('81b6b1162708448c9c4c99023c53f615', '4587', 'Redmi Note 8', '145723595854525645', '79ca19a5e3dc45e3a93951323aa2dfd5', 'c3dd8db84b5b4e64929c2f91a2efaf0e'),
	('c11143032a924176b66c372b836d435a', '65823', '21"', '584725415655', '7d28aa7da389413cbc43300c8127e61c', '08ac3d59cd17426ca9b2fe90ac33ba4b');
/*!40000 ALTER TABLE "inventario_recurso" ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
