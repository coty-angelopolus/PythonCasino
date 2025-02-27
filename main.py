import random

current_user = ""
cards_out = []


def Casino_TUI():
    print("*****************Casino TUI**************************")
    print("\n\nWhat would you like to do?")
    print("\n1 - Blackjack\n2 - Poker\n3 - Quit")
    usersel2 = input("\n> ")
    if usersel2 == "1":
        print("Loading Blackjack")
        Blackjack()
    elif usersel2 == "2":
        print("Loading Poker")
        Poker()
    elif usersel2 == "3":
        print("Goodbye!")
        quit()

def Blackjack():
    print("Welcome to Blackjack!")
    print("How much would you like to wager?")
    user_bet_amount = input("\n> ")
    try:
        user_bet_amount = int(user_bet_amount)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        Blackjack()
    if user_bet_amount > get_player_amount():
        print("You don't have enough money to wager that amount")
        Blackjack()

    print("Great, let's play!")
    print(card_handler())
    print(card_handler())
    print(card_handler())
    user_cards = []
    dealer_cards = []







def card_handler():
    global cards_out
    random_number = random.randint(1, 52)
    while random_number in cards_out:
        random_number = random.randint(1, 52)
    cards_out.append(random_number)
    card = random_number
    suits = ["hearts", "diamonds", "spades", "clubs"]
    ranks = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]

    suit_index = (card - 1) // 13  # Determine suit (0-3)
    rank_index = (card - 1) % 13  # Determine rank (0-12)

    return f"{ranks[rank_index]} of {suits[suit_index]}"



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


def decipher(identifier,text):
        # 1 for decoding. 2 for encoding
    if identifier == 1:
        encoded = "".join(chr(ord(char) + 3) for char in text)  # Shift each letter by +3 ASCII
        return encoded
    elif identifier == 2:
        decoded = "".join(chr(ord(char) - 3) for char in text)  # Reverse the shift (-3)
        return decoded
    else:
        print("pick one or two")



def main():

    print("Hello everyone and welcome to my casino project that uses AI to simulate other players and betters")
    print("\nThis is a work in progress that is for training anf for fun that I will continue to build upon")
    print("\nFirst commit is on 2/26/25. Created by Coty Angelopolus using Gemini api")

    input("\nPress enter to login or create an account")

    account_login()

if __name__ == '__main__':
    main()


