import random
import string

# Global strings to be used to randomly generate password components
string_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string_num = '0123456789'
string_special = '~!@#$%^&*()'

def userInput():
    length = int(input("Enter the length of the password: "))
    use_numbers = input("Include numbers?(yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters?(yes/no):").lower() == 'yes'
    return(length, use_special_chars, use_numbers)

# Update the code below below this line
def generate_password(length, use_special_chars, use_numbers):
    """Generates a random password based on user preferences."""
    password = ''

    # Generate remaining characters
    while length>2:
        password += random.choice(string_char)
        length-=1

    # Replace second last character with number if required
    if use_numbers:
        password+=random.choice(string_num)
    else:
        password+=random.choice(string_char)

    # Replace last character with special character if required
    if use_special_chars:
        password+=random.choice(string_special)
    else:
        password+=random.choice(string_char)

    return password


if __name__ == '__main__':
    length, use_special_chars, use_numbers = userInput()
    generated_password = generate_password(length, use_special_chars, use_numbers)
    print("\nGenerated Password:", generated_password)