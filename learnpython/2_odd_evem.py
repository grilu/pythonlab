# Main program starts here
def main():
    # Ask the user for a number and check if it's even or odd
    number = int(input("Enter a number: "))
    if number % 4 == 0:
        print("The number is a multiple of 4 and even.")
    elif number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

    # Extras: Check how one number divides into another
    num = int(input("Enter another number (num) to check: "))
    check = int(input("Enter a number (check) to divide by: "))
    if num % check == 0:
        print(f"{num} divides evenly by {check}.")
    else:
        print(f"{num} does not divide evenly by {check}.")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
