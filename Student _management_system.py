import json
import os

FILE_NAME = "students.json"


class Student:
    def __init__(self, student_id, name, age, course, email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.email = email

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "email": self.email
        }


class StudentManager:
    def __init__(self):
        self.students = self.load_students()

    def load_students(self):
        try:
            if os.path.exists(FILE_NAME):
                with open(FILE_NAME, "r") as file:
                    return json.load(file)
        except (json.JSONDecodeError, OSError):
            pass
        return []

    def save_students(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self):
        student_id = input("Enter Student ID: ")
        if any(s["id"] == student_id for s in self.students):
            print("Student ID already exists.")
            return

        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")
        email = input("Enter Email: ")

        student = Student(student_id, name, age, course, email)
        self.students.append(student.to_dict())
        self.save_students()
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        for s in self.students:
            print(
                f'ID: {s["id"]} | Name: {s["name"]} | '
                f'Age: {s["age"]} | Course: {s["course"]} | '
                f'Email: {s["email"]}'
            )

    def search_student(self):
        keyword = input("Enter ID, name, course, or email: ").lower()

        results = [
            s for s in self.students
            if keyword in s["id"].lower()
            or keyword in s["name"].lower()
            or keyword in s["course"].lower()
            or keyword in s["email"].lower()
        ]

        if not results:
            print("No matching student found.")
            return

        for s in results:
            print(
                f'ID: {s["id"]} | Name: {s["name"]} | '
                f'Age: {s["age"]} | Course: {s["course"]} | '
                f'Email: {s["email"]}'
            )

    def update_student(self):
        student_id = input("Enter Student ID to update: ")

        for student in self.students:
            if student["id"] == student_id:
                name = input("Enter new name: ")
                age = input("Enter new age: ")
                course = input("Enter new course: ")
                email = input("Enter new email: ")

                if name:
                    student["name"] = name
                if age:
                    student["age"] = age
                if course:
                    student["course"] = course
                if email:
                    student["email"] = email

                self.save_students()
                print("Student updated successfully.")
                return

        print("Student not found.")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")

        for student in self.students:
            if student["id"] == student_id:
                self.students.remove(student)
                self.save_students()
                print("Student deleted successfully.")
                return

        print("Student not found.")


def main():
    manager = StudentManager()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.update_student()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            manager.search_student()
        elif choice == "6":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
