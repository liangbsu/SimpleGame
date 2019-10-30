
import random

user = input("Do you want play game? [Y/N] ").lower()

while user != "n":
    number = random.randint(0, 6)
    guess = 0
    guess_limit = 3
    print("I am thinking about a number, from 0 to 6!")

    try:
        while guess < guess_limit:
            if guess == 0:
                print("You have 3 guess.")
            elif guess == 1:
                print("You have 2 guess.")
            else:
                print("You have 1 guess.")
            user_guess = int(input("Let type your number: "))
            if user_guess == number:
                print("\nYealll, You win!!")
                break
            elif user_guess > number and guess < 2:
                print("\nToo big!!")
                print("Try again!")

            elif user_guess < number and guess < 2:
                print("\nToo small!!")
                print("Try again!")
            guess += 1
        else:
            print("\nSorry!! You failed.")
    except:
        print("Sorry, It's must be number.")
        print("Try again.")

    user = input("\nDo you want play again? [Y/N] ").lower()
if user == "n":
    print("\nThank you. See you next time.")






