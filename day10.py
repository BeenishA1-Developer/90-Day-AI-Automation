import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    
    try:
        length = int(input("Enter password length (min 8): "))
        if length < 8:
            print("Too short! Using minimum 8.")
            length = 8
    except ValueError:
        print("Invalid input! Using default length 12.")
        length = 12
    
    print(f"\nGenerated Password: {generate_password(length)}")
    print("Keep it safe!")

main()