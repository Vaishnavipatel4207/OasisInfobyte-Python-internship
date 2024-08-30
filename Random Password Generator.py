import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    if not (use_letters or use_numbers or use_symbols):
        raise ValueError("At least one character type must be selected")
    
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("No characters available for password generation")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            raise ValueError("Length must be a positive integer")
        
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
