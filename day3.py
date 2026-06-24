marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    print("Grade: A — Excellent!")
elif marks >= 80:
    print("Grade: B — Good!")
elif marks >= 70:
    print("Grade: C — Average")
elif marks >= 60:
    print("Grade: D — Below Average")
else:
    print("Grade: F — Failed")