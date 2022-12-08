import random
import sys

RAND_NUM = random.randint(1, 99)
LUCKY_NUM = 42

def ask_user():
    number = 0
    inc = 0
    while number != RAND_NUM:
        inc+=1
        if (user_input := input("What's your guess between 1 and 99?\n>> ")) == "exit":
            sys.exit()
        try:
            number = int(user_input)
        except ValueError:
            print("You need to enter only integer values")
            sys.exit()
        if number > RAND_NUM:
            print("Too high!")
        elif number < RAND_NUM:
            print("Too low!")
    return inc

def main():
    print("This is an interactive guessing game!\n" +
        "You have to enter a number between 1 and 99 to find out the secret number.\n" +
        "Type 'exit' to end the game.\n" +
        "Good luck!")
    count = ask_user()
    if RAND_NUM == LUCKY_NUM:
        print("The answer to the ultimate question of life, the universe and everything is 42")
    print("Congratulations, you've got it!")
    if count != 1:
        print(f"You won in {count} attemps!")
    else:
        print("You found it on first try! Amazing!")

if __name__ == '__main__':
    main()
