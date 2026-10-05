-- Script: 01_init_db.sql
-- Propósito: Creación de Base de Datos, Usuario y Asignación de Privilegios
-- Proyecto: API de Finanzas Personales (DRF)
-- 1. Creación de la Base de Datos
CREATE DATABASE db_finanzas
    WITH 
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Chile.1252'
    LC_CTYPE = 'Spanish_Chile.1252'
    TEMPLATE = template0;
-- 2. Creación del Usuario / Rol de Servicio para la API
CREATE USER user_finanzas WITH PASSWORD 'Finanzas2026@';
-- 3. Configuración de Parámetros de Sesión Recomendados para Django
ALTER ROLE usr_finanzas SET client_encoding TO 'utf8';
ALTER ROLE usr_finanzas SET default_transaction_isolation TO 'read committed';
ALTER ROLE usr_finanzas SET timezone TO 'UTC';
-- 4. Otorgamiento de Privilegios
GRANT ALL PRIVILEGES ON DATABASE db_finanzas_drf TO usr_finanzas;