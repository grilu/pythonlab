import random
import string


def generate_password(length, complexity=3):
    """Generates a random password based on the specified complexity and length."""
    character_sets = {
        1: string.ascii_lowercase,  # Weak: only lowercase letters
        2: string.ascii_letters,  # Medium: lowercase and uppercase letters
        3: string.ascii_letters + string.digits,  # Strong: letters and numbers
        4: string.ascii_letters + string.digits + string.punctuation  # Very Strong: letters, numbers, and symbols
    }

    # Choose the character set based on the desired complexity, default to the highest if out of range
    characters = character_sets.get(complexity, character_sets[4])

    # Create a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def get_user_input():
    """Asks the user for their desired password strength and length."""
    print("Choose the strength of your password:")
    print("1: Weak (lowercase letters only)")
    print("2: Medium (mixed case letters)")
    print("3: Strong (mixed case letters and numbers)")
    print("4: Very Strong (mixed case letters, numbers, and symbols)")
    complexity = int(input("Enter the strength level (1-4): "))
    length = int(input("How long do you want your password to be? "))
    return length, complexity


def main():
    length, complexity = get_user_input()
    password = generate_password(length, complexity)
    print("Your generated password is:", password)


if __name__ == "__main__":
    main()
