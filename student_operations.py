"""
student_operations.py
----------------------
All CRUD operations for students — done through SQLAlchemy ORM methods
(session.add, session.query, .filter, .delete) instead of raw SQL.
"""

from db import get_session
from models import Student


# ---------------------------------------------------------------------
# CREATE — Add a new student
# ---------------------------------------------------------------------
def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    email = input("Enter email: ")
    marks = input("Enter marks: ")

    session = get_session()
    if not session:
        return
    try:
        new_student = Student(
            name=name,
            age=int(age) if age else None,
            course=course,
            email=email,
            marks=float(marks) if marks else None
        )
        session.add(new_student)
        session.commit()
        print("✅ Student added successfully.")
    except Exception as e:
        print("❌ Error adding student:", e)
        session.rollback()
    finally:
        session.close()


# ---------------------------------------------------------------------
# READ — View all students
# ---------------------------------------------------------------------
def view_students():
    session = get_session()
    if not session:
        return
    try:
        students = session.query(Student).order_by(Student.student_id).all()

        if not students:
            print("No records found.")
            return

        print(f"\n{'ID':<5}{'Name':<20}{'Age':<6}{'Course':<20}{'Email':<25}{'Marks':<8}")
        print("-" * 84)
        for s in students:
            print(f"{s.student_id:<5}{s.name:<20}{s.age or '':<6}{s.course or '':<20}{s.email or '':<25}{s.marks or '':<8}")
        print()
    except Exception as e:
        print("❌ Error fetching students:", e)
    finally:
        session.close()


# ---------------------------------------------------------------------
# READ — Search a student by ID
# ---------------------------------------------------------------------
def search_student():
    student_id = input("Enter Student ID to search: ")
    session = get_session()
    if not session:
        return
    try:
        student = session.query(Student).filter(Student.student_id == student_id).first()
        if student:
            print(f"\n{student}\n")
        else:
            print("No student found with that ID.")
    except Exception as e:
        print("❌ Error searching student:", e)
    finally:
        session.close()


# ---------------------------------------------------------------------
# UPDATE — Modify a student's details
# ---------------------------------------------------------------------
def update_student():
    student_id = input("Enter Student ID to update: ")

    session = get_session()
    if not session:
        return
    try:
        student = session.query(Student).filter(Student.student_id == student_id).first()
        if not student:
            print("No student found with that ID.")
            return

        print("Leave field blank to keep the current value.")
        name = input("New name: ")
        age = input("New age: ")
        course = input("New course: ")
        email = input("New email: ")
        marks = input("New marks: ")

        if name:
            student.name = name
        if age:
            student.age = int(age)
        if course:
            student.course = course
        if email:
            student.email = email
        if marks:
            student.marks = float(marks)

        session.commit()
        print("✅ Student updated successfully.")
    except Exception as e:
        print("❌ Error updating student:", e)
        session.rollback()
    finally:
        session.close()


# ---------------------------------------------------------------------
# DELETE — Remove a student record
# ---------------------------------------------------------------------
def delete_student():
    student_id = input("Enter Student ID to delete: ")
    session = get_session()
    if not session:
        return
    try:
        student = session.query(Student).filter(Student.student_id == student_id).first()
        if not student:
            print("No student found with that ID.")
            return

        confirm = input(f"Are you sure you want to delete student {student_id}? (y/n): ")
        if confirm.lower() != 'y':
            print("Deletion cancelled.")
            return

        session.delete(student)
        session.commit()
        print("✅ Student deleted successfully.")
    except Exception as e:
        print("❌ Error deleting student:", e)
        session.rollback()
    finally:
        session.close()