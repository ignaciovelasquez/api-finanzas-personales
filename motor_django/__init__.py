from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.mysql.features import DatabaseFeatures

# 1. Omitir la validación estricta de versión de MariaDB
BaseDatabaseWrapper.check_database_version_supported = lambda self: None

# 2. Desactivar RETURNING para máxima compatibilidad con MariaDB 10.4 de XAMPP
DatabaseFeatures.can_return_columns_from_insert = property(lambda self: False)
DatabaseFeatures.can_return_rows_from_bulk_insert = property(lambda self: False)