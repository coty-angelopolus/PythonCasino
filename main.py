current_user = ""


def Casino_TUI():
    print("*****************Casino TUI**************************")
    print("\n\nWhat would you like to do?")



def set_account_updater(change):
    global current_user
    try:
        newamount = 0
        with open("players_login.txt", "r") as file:
            lines = file.readlines()

        for i in range(len(lines)):
            if current_user in lines[i].strip():
                newamount = str(get_player_amount() + int(change))
                lines[i+2] = newamount
                break
        with open("players_login.txt", "w") as file:
            file.writelines(lines)

        print(current_user + "'s total has been updated.\nNew total: "+ newamount)
    except FileNotFoundError:
        print("error loading player login file")


def get_player_amount():
    global current_user
    amount_return = 0
    try:
        with open("players_login.txt", "r") as file:
            lines = file.readlines()

            for i in range(len(lines)):
                if lines[i].strip() == current_user:
                    amount_return = int(lines[i + 2].strip())

    except FileNotFoundError:
        print("error loading player login file")

    return amount_return

def account_login():
    global current_user
    print("do you have an account associated with clam betting?")
    print("Y or N")
    usersel1 = input("\n> ").lower()
    if usersel1 == "y":
        print("Enter in your username")
        player_username = input("\n> ")

        try:
            with open(f"players_login.txt", "r") as file:
                lines = file.readlines()  # Read all lines into a list

                for i in range(len(lines)):
                    if player_username in lines[i].strip():
                        print("\nAccount found!\nEnter in your password")
                        user_password = input("\n> ")
                        if lines[i + 1].strip() == user_password:
                            print("Account login successful")
                            current_user = player_username
                            print("Account Value: "+ str(get_player_amount()))
                            Casino_TUI()


        except FileNotFoundError:
            print("error loading player login file")

    elif usersel1 == "n":
        print("\nEnter in your username\n")
        user_username = input("\n> ")
        print("\nEnter in your password\n")
        user_password = input("\n> ")
        print("Welcome to Clam Betting "+ user_username + "!\nHow much money do you want to put in your account?")
        while True:
            try:
                user_deposit = int(input("\n> "))
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")
        with open("players_login.txt", "a") as file:
            file.write(user_username + "\n")
            file.write(user_password + "\n")
            file.write(str(user_deposit) + "\n")
        print("Account created successfully!")
        current_user = user_username
        Casino_TUI()

    else:
        print("Please enter Y or N")
        account_login()




def main():

    print("Hello everyone and welcome to my casino project that uses AI to simulate other players and betters")
    print("\nThis is a work in progress that is for training anf for fun that I will continue to build upon")
    print("\nFirst commit is on 2/26/25. Created by Coty Angelopolus using Gemini api")

    input("\nPress enter to login or create an account")

    account_login()

if __name__ == '__main__':
    main()


