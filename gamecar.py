
user = input("Do you want play game? [Y/N] ").lower()
begin = 1
while user != "n":
    if begin == 1:
        print("""
                    Start - to start car
                    Stop - to stop car
                    Quit - to quit game
                    Help - to print this again
                    """)
        begin += 1

    status_car = False

    while True:
        input_user = input(">> ").lower()
        if input_user == "start":
            if status_car:
                print("Car already start!")
            else:
                print("Car start.")
                status_car = True
        elif input_user == "stop":
            if status_car:
                print("Car stop.")
                status_car = False
            else:
                print("Car already stop!")
        elif input_user == "quit":
            if status_car:
                print("Sorry!")
                print("You must stop car to quit.")
            else:
                user = input("Do you want play game again? [Y/N] ")
                break
        elif input_user == "help":
            print("""
            Start - to start car
            Stop - to stop car
            Quit - to quit game
            Help - to print this again
            """)
        else:
            print("Sorry, I don't understand!")

if user == "n":
    print("Thank you. See you next time.")
