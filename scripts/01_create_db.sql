-- ====================================================================
-- EVIDENCIA 1: Creación de la Base de Datos MySQL
-- Proyecto: API de Finanzas Personales
-- ====================================================================

CREATE DATABASE IF NOT EXISTS finanzas_db 
    CHARACTER SET utf8mb4 
    COLLATE utf8mb4_unicode_ci;

    -- ====================================================================
-- Creación del Usuario de Aplicación MySQL
CREATE USER IF NOT EXISTS 'finanzas_user'@'localhost' 
    IDENTIFIED BY 'Futbol123';

-- ====================================================================
-- creación de la Asignación de Privilegios
GRANT ALL PRIVILEGES ON finanzas_db.* TO 'finanzas_user'@'localhost';
FLUSH PRIVILEGES;