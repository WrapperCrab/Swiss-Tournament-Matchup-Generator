from colorama import Fore, Back, Style

players = [] # player = [matches, lives]
ongoingMatches = [] # match = [playerIndex1, playerIndex2]

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
        print("2) Display Players")

        print("3) Generate Best Next Matchups")

        print("4) Set Ongoing Match")
        print("5) Display Ongoing Matches")

        print("6) Set Match Result")
        print("7) Display Match Results")

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
                case 2:
                    display_players()
                # case 3:
                #     generate_matchups_menu()
                case 4:
                    set_ongoing_match()
                case 5:
                    display_ongoing_matches()

                case _:
                    print(Fore.RED + "That was not a valid option")
                    print(Style.RESET_ALL)
        else:
            print(Fore.RED + "That was not a valid option")
            print(Style.RESET_ALL)

def add_players_menu():
    # Ask how many players the user wants to add
    print("How many players would you like to add?")
    numPlayers = input()
    if numPlayers.isdigit():
        numPlayersInt = int(numPlayers)
        add_players(numPlayersInt)
        print(Fore.GREEN + numPlayers + " player added successfully!")
        print(Style.RESET_ALL)
    else:
        print(Fore.RED + "That was not a valid input")
        print(Style.RESET_ALL)
def add_players(numPlayers: int):
    for i in range(numPlayers):
        players.append([0,2])

def set_ongoing_match():
    # Have the player type the indeces of two players and save it as an ongoing match
    # Check if the pairing is legal (i.e. neither player is already in a match)
    print("Who is the first player?")
    player1Index = input()
    print("Who is the second player?")
    player2Index = input()

    if player1Index.isdigit() and player2Index.isdigit():
        player1Index = int(player1Index)
        player2Index = int(player2Index)
        for match in ongoingMatches:
            if (player1Index in match) or (player2Index in match):
                print(Fore.RED + "One of those players is already in an ongoing match")
                print(Style.RESET_ALL)
                return
        ongoingMatches.append([player1Index, player2Index])
        print(Fore.GREEN + "The match between " + str(player1Index) + " and " + str(player2Index) + " has been added!")
        print(Style.RESET_ALL)
    else:
        print(Fore.RED + "Please enter integers")
        print(Style.RESET_ALL)
def display_ongoing_matches():
    for match in ongoingMatches:
        print(str(match[0]) + " is facing " + str(match[1]))


# def generate_matchups_menu():
#     keepgoing = True
#     while keepgoing:
#         print("")
#         print("What matchup would you like to generate?")
#         print("1) Best Matchups")
#         print("2) Best Matchups With Player")

#         print("0) Exit Matchup Generation")
#         print("")


#         choice = input()
#         if choice.isdigit():
#             choice = int(choice)
#             match choice:
#                 case 0:
#                     keepgoing = False
#                 case 1:
#                     print("How many first players should by tried?")
#                     numFirstPlayers = input()
#                     print("How many second players should be tried?")
#                     numSecondPlayers = input()

#                     if numFirstPlayers.isdigit() and numSecondPlayers.isdigit():
#                         numFirstPlayers = int(numFirstPlayers)
#                         numSecondPlayers = int(numSecondPlayers)
#                         display_best_matchups(numFirstPlayers, numSecondPlayers)
#                     else:
#                         print("Input numbers stupid")
#                 case _:
#                     print("That was not a valid option")
#         else:
#             print("That was not a valid option")
# def display_best_matchups(numFirstPlayers: int, numSecondPlayers: int):
#     matchups = []

# def get_best_matchup(player1Index = -1, excludeIndeces = []):
#     # Finds the best matchup satisfying all the restrictions set in the parameters
    
#     if player1Index!=-1:
#         index1 = player1Index
#     else:
#         index1 = find_primed_player_index(excludeIndeces)

#     newExcludeIndeces = list( set(excludeIndeces).union(set([index1])) )
#     index2 = find_primed_player_index(newExcludeIndeces)

#     return [index1, index2]

# def find_primed_player_index(excludeIndeces = []):
#     # Finds the player with the fewest matches and fewest lives. We call this the primed player
#     primedPlayer = -1
#     for i in range(len(players)):
#         if i in excludeIndeces:
#             continue
#         if primedPlayer == -1:
#             primedPlayer = i
#             continue
#         if (players[i][0] < players[primedPlayer][0]) or ((players[i][0] == players[primedPlayer][0]) and (players[i][1] < players[primedPlayer][1])):
#             primedPlayer = i
#     return primedPlayer


def display_players():
    print(f"{"Name":^10} {"Matches":^10} {"Lives":^10}")
    for i in range(len(players)):
        # name = int_to_letter(i)
        name = i
        print(f"{name:^10} {players[i][0]:^10} {players[i][1]:^10}")



# Helper functions
# def int_to_letter(value):
#     # Maps integers to capital letters. 0 to A, 1 to B, etc.
#     #!!! Values greater than 25 will no longer be letters
#     return chr(value + ord("A"))

if __name__=='__main__':
    main()