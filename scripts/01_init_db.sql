-- Script: 01_init_db.sql
-- Propósito: Creación de Base de Datos, Usuario y Asignación de Privilegios
-- Proyecto: API de Finanzas Personales (DRF)
-- 1. Creación de la Base de Datos
CREATE DATABASE IF NOT EXISTS finanzas_db 
    CHARACTER SET utf8mb4 
    COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'finanzas_user'@'localhost' 
    IDENTIFIED BY 'Futbol123';

GRANT ALL PRIVILEGES ON finanzas_db.* TO 'finanzas_user'@'localhost';

FLUSH PRIVILEGES;