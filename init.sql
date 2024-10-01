-- Ejemplos de cómo conectarse y crear tablas en postgres

-- Usar imagen oficial de postgres en dockerhub https://hub.docker.com/_/postgres

-- Clonar la imagen con el comando 'docker pull postgres'

-- Ejecutar 'docker run -p 5432:5432 -e POSTGRES_PASSWORD="postgres",POSTGRES_USER="postgres" postgres'

-- Abrir terminal desde el contenedor (o escribir en terminal del computador 'docker exec -it <nombre_contenedor> bash')

--Crear tabla rendicion
CREATE TABLE Rendicion (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    monto FLOAT NOT NULL
);

--Insertar dato (fecha: aaaa-mm-dd (ISO8601))
INSERT INTO rendicion (fecha, monto) VALUES ('2024-01-01', '250000');
INSERT INTO rendicion (fecha, monto) VALUES ('2024-01-01', '532100');

--Mostrar todas las rendiciones
SELECT * FROM rendicion;


