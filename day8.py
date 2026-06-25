def save_note(note):
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("Note saved!")

def read_notes():
    try:
        with open("notes.txt", "r") as f:
            notes = f.readlines()
        if not notes:
            print("No notes found.")
        else:
            print("\n=== Your Notes ===")
            for i, note in enumerate(notes, 1):
                print(f"{i}. {note.strip()}")
    except FileNotFoundError:
        print("No notes file found. Add a note first.")

def main():
    print("=== Notes App ===")
    print("1. Add Note")
    print("2. Read Notes")
    choice = input("Choose (1/2): ")
    
    if choice == "1":
        note = input("Enter your note: ")
        save_note(note)
    elif choice == "2":
        read_notes()
    else:
        print("Invalid choice!")

main()