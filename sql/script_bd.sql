-- 1. Crear la base de datos
CREATE DATABASE db_backend CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 2. Crear el usuario para MySQL/MariaDB
CREATE USER 'user_backend'@'localhost' IDENTIFIED BY 'Password*';

-- 3. Asignar permisos completos al usuario sobre la base de datos
GRANT ALL PRIVILEGES ON db_backend.* TO 'user_backend'@'localhost';

-- 4. Aplicar los cambios de privilegios
FLUSH PRIVILEGES;