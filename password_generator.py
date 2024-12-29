import random
import string

def generate_password(length):
    """
    Generates a secure random password based on the specified length.

    :param length: The desired length of the password (minimum 4).
    :return: A randomly generated password as a string.
    """
    # Ensure the password length is valid
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    # Define character categories
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure at least one character from each category
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Fill the rest of the password with random choices from all categories
    all_characters = uppercase + lowercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Return the password as a string
    return ''.join(password)

def main():
    """
    Main function to interact with the user and generate a password.
    """
    print("Welcome to the Random Password Generator!")
    print("This tool generates secure and random passwords for your needs.")
    
    while True:
        try:
            # Ask the user for the desired password length
            length = int(input("Enter the desired password length (minimum 4): "))
            
            # Generate the password
            password = generate_password(length)
            print(f"Your generated password is: {password}")
            break
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid number.")

if __name__ == "__main__":
    main()