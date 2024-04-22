choice1 = input("Option?")
choice2 = input("Option?")

if choice1 == choice2:
    print("It's a tie!")
elif (choice1 == 'rock' and choice2 == 'scissors') or \
     (choice1 == 'scissors' and choice2 == 'paper') or \
     (choice1 == 'paper' and choice2 == 'rock'):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")