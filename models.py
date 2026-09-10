"""
models.py
---------
Defines the Student table as a Python class (ORM model).
No SQL is written here — SQLAlchemy converts this class into a table.
"""

from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    course = Column(String(100))
    email = Column(String(100), unique=True)
    marks = Column(Numeric(5, 2))

    def __repr__(self):
        return (f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | "
                f"Course: {self.course} | Email: {self.email} | Marks: {self.marks}")