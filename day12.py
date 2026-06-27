# day12.py — JSON Data Handler
import json

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print("Data saved!")

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("No data found!")
        return {}

def main():
    students = [
        {"name": "Ali", "marks": 85},
        {"name": "Sara", "marks": 92},
        {"name": "Ahmed", "marks": 78}
    ]
    
    save_data("students.json", students)
    
    loaded = load_data("students.json")
    for s in loaded:
        print(f"{s['name']}: {s['marks']}")

main()