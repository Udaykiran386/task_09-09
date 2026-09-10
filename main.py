"""
main.py
-------
Entry point for the Student Management System.
Run this file: python main.py
"""

from db import create_table
from student_operations import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)


def main():
    create_table()

    while True:
        print("""
========= STUDENT MANAGEMENT SYSTEM =========
1. Add Student
2. View All Students
3. Search Student by ID
4. Update Student
5. Delete Student
6. Exit
===============================================
        """)
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()