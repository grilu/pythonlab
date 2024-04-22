import random

num = random.randrange(1, 10)
print("Random number is ", num)

while True:
    usernum = input("Enter a number or type 'exit' to quit: ")
    if usernum == "exit":
        break
    try:
        usernum = int(usernum)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if usernum == num:
        print("You guessed it right!")
        break
    elif usernum < num:
        print("Your number is lower than the number")
    else:
        print("Your number is higher than the number")

