


def Casino_TUI():
    print("*****************Casino TUI**************************")
    print("\n\nWhat would you like to do?")


def account_login():
    print("do you have an account associated with clam betting?")
    print("Y or N")
    usersel1 = input("\n> ").lower()
    if usersel1 == "y":
        print("Enter in your username")
        player_username = input("\n> ")
        try:
            with open(f"players_login.txt", "r") as file:
                for line in file

    elif usersel1 == "n":
        print("You do not have an account")
    else:
        print("Please enter Y or N")




def main():

    print("Hello everyone and welcome to my casino project that uses AI to simulate other players and betters")
    print("\nThis is a work in progress that is for training anf for fun that I will continue to build upon")
    print("\nFirst commit is on 2/26/25. Created by Coty Angelopolus using Gemini api")

    input("\nPress enter to login or create an account")

    account_login()


    Casino_TUI()


if __name__ == '__main__':
    main()


