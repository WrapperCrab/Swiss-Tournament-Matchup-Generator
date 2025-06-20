
players = []
# player = [matches, lives]

def main():
    # Show the main menu
    print("Welcome to the Swiss Tournament Matchup Generator")
    menu()

def menu():
    keepgoing = True
    while keepgoing:
        print("")
        print("What would you like to do?")
        print("1) Add Players")
        print("2) Generate Best Next Matchups")
        print("3) Set Ongoing Match")
        print("4) Set Match Result")
        print("5) Display Player Statuses")
        print("6) Display Completed Matches")

        print("0) Exit Program")
        print("")


        choice = input()
        if choice.isdigit():
            choice = int(choice)
            match choice:
                case 0:
                    keepgoing = False
                    print("Good Luck!")
                case 1:
                    add_players_menu()
                case 5:
                    display_players()
                case _:
                    print("That was not a valid option")
        else:
            print("That was not a valid option")

def add_players_menu():
    # Ask how many players the user wants to add
    print("How many players would you like to add?")
    numPlayers = input()
    if numPlayers.isdigit():
        numPlayersInt = int(numPlayers)
        if numPlayersInt > 0:
            add_players(numPlayersInt)
            print(numPlayers + " player added successfully!")
        else:
            print("Only positive values plz")
    else:
        print("That was not a valid input")

    pass
def add_players(numPlayers):
    for i in range(numPlayers):
        players.append([0,2])

def display_players():
    print(f"{"Name":^10} {"Matches":^10} {"Lives":^10}")
    for i in range(len(players)):
        name = int_to_letter(i)
        print(f"{name:^10} {players[i][0]:^10} {players[i][1]:^10}")



# Helper functions
def int_to_letter(value):
    # Maps integers to capital letters. 0 to A, 1 to B, etc.
    #!!! Values greater than 25 will no longer be letters
    return chr(value + ord("A"))


if __name__=='__main__':
    main()