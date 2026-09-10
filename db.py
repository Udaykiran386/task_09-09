"""
db.py
-----
Sets up the SQLAlchemy engine and session, and creates tables
from the ORM models (no raw SQL needed).

Libraries used:
    pip install sqlalchemy psycopg2-binary
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
from models import Base


def get_engine():
    try:
        engine = create_engine(DATABASE_URL)
        return engine
    except Exception as e:
        print("❌ Error creating engine:", e)
        return None


def create_table():
    """Creates all tables defined in models.py if they don't exist."""
    engine = get_engine()
    if not engine:
        return
    Base.metadata.create_all(engine)
    print("✅ Table 'students' is ready.")


def get_session():
    """Returns a new database session for performing operations."""
    engine = get_engine()
    if not engine:
        return None
    Session = sessionmaker(bind=engine)
    return Session()