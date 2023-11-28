import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            password_length = int(input("Enter the length of the password: "))
            if password_length <= 0:
                print("Please enter a positive length.")
                continue

            num_passwords = int(input("Enter the number of passwords to generate: "))
            if num_passwords <= 0:
                print("Please enter a positive number of passwords.")
                continue

            for _ in range(num_passwords):
                password = generate_password(password_length)
                print(f"Generated Password: {password}")

            break
        except ValueError:
            print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
