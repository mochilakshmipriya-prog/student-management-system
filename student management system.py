import sqlite3

# Connect to database
connection = sqlite3.connect("students.db")
cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL
)
""")

connection.commit()


# Add student
def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")

    cursor.execute("""
    INSERT INTO students (name, age, course, email, phone)
    VALUES (?, ?, ?, ?, ?)
    """, (name, age, course, email, phone))

    connection.commit()

    print("Student added successfully!")


# View students
def view_students():
    print("\n--- Student List ---")

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No students found.")
        return

    for student in students:
        print("--------------------------------")
        print("ID     :", student[0])
        print("Name   :", student[1])
        print("Age    :", student[2])
        print("Course :", student[3])
        print("Email  :", student[4])
        print("Phone  :", student[5])


# Search student
def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter student ID: ")

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("--------------------------------")
        print("ID     :", student[0])
        print("Name   :", student[1])
        print("Age    :", student[2])
        print("Course :", student[3])
        print("Email  :", student[4])
        print("Phone  :", student[5])
    else:
        print("Student not found.")


# Update student
def update_student():
    print("\n--- Update Student ---")

    student_id = input("Enter student ID: ")

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        return

    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    course = input("Enter new course: ")
    email = input("Enter new email: ")
    phone = input("Enter new phone number: ")

    cursor.execute("""
    UPDATE students
    SET name = ?, age = ?, course = ?, email = ?, phone = ?
    WHERE id = ?
    """, (name, age, course, email, phone, student_id))

    connection.commit()

    print("Student updated successfully!")


# Delete student
def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter student ID: ")

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        return

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    connection.commit()

    print("Student deleted successfully!")


# Main menu
def main():
    while True:
        print("\n================================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run program
if __name__ == "__main__":
    main()

# Close database
connection.close()