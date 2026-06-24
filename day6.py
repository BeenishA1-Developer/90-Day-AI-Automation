students = []

def add_student(name, marks):
    student = {"name": name, "marks": marks}
    students.append(student)
    print(f"Student '{name}' added successfully!")

def show_all():
    if not students:
        print("No students found.")
        return
    print("\n=== All Students ===")
    for i, s in enumerate(students, 1):
        grade = "Pass" if s["marks"] >= 50 else "Fail"
        print(f"{i}. {s['name']} | Marks: {s['marks']} | {grade}")

def main():
    add_student("Ali", 85)
    add_student("Sara", 45)
    add_student("Ahmed", 72)
    show_all()

main()