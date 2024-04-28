import random

def getnum():
    num = 4
    return num

def main():
    a = getnum()
    rand = 50
    count = 0

    while a != rand:
        count += 1
        if a < rand:
            print("A is lower than rand")
            # Ensure there's a valid range for randint
            new_upper = int(rand / 2)
            rand = random.randint(1, max(new_upper, 2))
        elif a > rand:
            print("A is higher than rand")
            # Ensure there's a valid range for randint
            new_upper = int(rand * 1.5)
            rand = random.randint(1, max(new_upper, a + 1))
        else:
            print(f"You guessed a is {a}")

    print(f"You guessed a is {a}. It took {count} attempts.")

if __name__ == '__main__':
    main()
