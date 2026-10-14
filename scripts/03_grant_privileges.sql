-- ====================================================================
-- EVIDENCIA 3: Asignación de Permisos y Privilegios en MySQL
-- Proyecto: API de Finanzas Personales
-- ====================================================================

GRANT ALL PRIVILEGES ON finanzas_db.* TO 'finanzas_user'@'localhost';
FLUSH PRIVILEGES;