"""
config.py
---------
Database connection settings.
Edit these values to match the database you created in pgAdmin.
"""

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "database": "student_db",
    "user": "postgres",
    "password": "root"
}

# SQLAlchemy connection string built from the settings above
DATABASE_URL = (
    f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
) 