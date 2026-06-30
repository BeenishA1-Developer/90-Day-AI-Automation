# day14.py — Students Pass/Fail and File Handling

# 1. List of students
students = [
    {"name": "Ayesha", "marks": 85},
    {"name": "Zain", "marks": 42},
    {"name": "Fatima", "marks": 35}
]

# 2. Open file and process loop
with open("fail_students.txt", "w") as f:
    f.write("=== Fail Students List ===\n")
    print("=== Students Status ===")
    
    for s in students:
        if s["marks"] < 50:
            # Jo fail hain unhein terminal par bhi dikhao aur file mein bhi likho
            output = f"Name: {s['name']}, Marks: {s['marks']}\n"
            print(f"Fail -> {output.strip()}")
            f.write(output)
        else:
            # Jo pass hain unhein bas terminal par print karo
            print(f"Pass -> Name: {s['name']}, Marks: {s['marks']}")

print("\nTask Done! File 'fail_students.txt' check karo.")