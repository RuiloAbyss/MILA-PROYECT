-- Crear la base de datos MilaProyect con archivos .mdf y .ldf en la ubicación especificada
CREATE DATABASE MilaProyect
ON PRIMARY (
    NAME = MilaProyect_Data,
    FILENAME = 'D:\PROYECTOS\MILA PROYECT\DataBase\MilaProyect.mdf' -- Ruta para el archivo .mdf
)
LOG ON (
    NAME = MilaProyect_Log,
    FILENAME = 'D:\PROYECTOS\MILA PROYECT\DataBase\MilaProyect_Log.ldf' -- Ruta para el archivo .ldf
);
GO

-- Usar la base de datos MilaProyect
USE MilaProyect;

-- Crear la tabla usuario
CREATE TABLE usuario (
    username VARCHAR(50) PRIMARY KEY, -- Nombre de usuario único y clave primaria
    nombre VARCHAR(50),
    apellido1 VARCHAR(50),
    apellido2 VARCHAR(50),
    correo VARCHAR(100) UNIQUE, -- El correo debe ser único
    contrasena VARCHAR(100),
    nivel_acceso VARCHAR(10) CHECK (nivel_acceso IN ('admon', 'asist'))
);
GO

-- Crear la función para verificar username o correo y contraseña
CREATE FUNCTION verificar_usuario(@usuario_input VARCHAR(100), @contrasena_input VARCHAR(100))
RETURNS NVARCHAR(50)
AS
BEGIN
    DECLARE @resultado NVARCHAR(50);

    IF EXISTS (SELECT 1 FROM usuario WHERE (username = @usuario_input OR correo = @usuario_input))
    BEGIN
        IF EXISTS (SELECT 1 FROM usuario WHERE (username = @usuario_input OR correo = @usuario_input) AND contrasena = @contrasena_input)
        BEGIN
            SET @resultado = 'Acceso permitido';
        END
        ELSE
        BEGIN
            SET @resultado = 'Contraseña incorrecta';
        END
    END
    ELSE
    BEGIN
        SET @resultado = 'Usuario no encontrado';
    END

    RETURN @resultado;
END;
GO