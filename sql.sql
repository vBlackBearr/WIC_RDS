-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS database_wic;
USE database_wic;

-- Creación de la tabla persona
CREATE TABLE IF NOT EXISTS persona (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    Telefono VARCHAR(15),
    Correo VARCHAR(255),
    Calle VARCHAR(255),
    Numero INT,
    Colonia VARCHAR(255),
    CP VARCHAR(10),
    Ciudad VARCHAR(255)
);

-- Creación de la tabla usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_persona INT,
    Contraseña VARCHAR(255) NOT NULL,
    PermisoAgenda BOOLEAN,
    FOREIGN KEY (id_persona) REFERENCES persona(id)
);




-- Creación de la tabla TipoPermiso
CREATE TABLE IF NOT EXISTS TipoPermiso (
    id INT AUTO_INCREMENT PRIMARY KEY,
    permiso VARCHAR(255) NOT NULL
);

insert into TipoPermiso VALUES (1, 'solo lectura'),(2, 'lectura y escritura'),(3, 'bloqueado');

-- Creación de la tabla PermisosPersonales
CREATE TABLE IF NOT EXISTS PermisosPersonales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    grantor INT,
    grantee INT,
    tipo_permiso_id INT,
    FOREIGN KEY (grantor) REFERENCES usuarios(id),
    FOREIGN KEY (grantee) REFERENCES usuarios(id),
    FOREIGN KEY (tipo_permiso_id) REFERENCES TipoPermiso(id)
);

-- Creación de la tabla AgendaUsuario
CREATE TABLE IF NOT EXISTS AgendaUsuario (
    usuario_id INT,
    persona_id INT,
    PRIMARY KEY (usuario_id, persona_id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (persona_id) REFERENCES persona(id)
);

-- Creación de la tabla TipoInvitacion
CREATE TABLE IF NOT EXISTS TipoInvitacion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(255) NOT NULL
);

insert into TipoInvitacion VALUES (1,'Persona invitando a otra a ver su agenda'),
(2,'Persona invitando a otra persona a ver la agenda de esa otra persona'),
(3,'Persona que invita a otra persona a hacer merge de sus agendas');

-- Creación de la tabla EstadoInvitaciones
CREATE TABLE IF NOT EXISTS EstadoInvitaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estado VARCHAR(255) NOT NULL
);

insert into EstadoInvitaciones VALUES (1,'pendiende'), (2,'concluida');

-- Creación de la tabla Invitaciones
CREATE TABLE IF NOT EXISTS Invitaciones (
    grantor INT,
    grantee INT,
    tipo_permiso_a_dar INT,
    tipo_invitacion_id INT,
    estado_invitacion_id INT,
    PRIMARY KEY (grantor, grantee),
    FOREIGN KEY (grantor) REFERENCES usuarios(id),
    FOREIGN KEY (grantee) REFERENCES usuarios(id),
    FOREIGN KEY (tipo_invitacion_id) REFERENCES TipoInvitacion(id),
    FOREIGN KEY (estado_invitacion_id) REFERENCES EstadoInvitaciones(id),
    FOREIGN KEY (tipo_permiso_a_dar) REFERENCES TipoPermiso(id)
);


