from colorama import Fore, Back, Style

players = [] # player = [matches, lives]
ongoingMatches = [] # match = [playerIndex1, playerIndex2]
completeMatches = [] # match = [playerIndexWin, playerIndexLose]

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
                case 6:
                    set_match_result()

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
    if not numPlayers.isdigit():
        print(Fore.RED + "That was not a valid input")
        print(Style.RESET_ALL)
        return

    numPlayersInt = int(numPlayers)
    add_players(numPlayersInt)
    print(Fore.GREEN + numPlayers + " player added successfully!")
    print(Style.RESET_ALL)

def add_players(numPlayers: int):
    for i in range(numPlayers):
        players.append([0,2])

def display_players():
    print(Fore.YELLOW + f"{"Index":^10} {"Matches":^10} {"Lives":^10}")
    for i in range(len(players)):
        matches = players[i][0]
        lives = players[i][1]
        if lives == 0:
            print(Fore.RED + f"{i:^10} {matches:^10} {lives:^10}" + Fore.YELLOW)
        else:
            print(f"{i:^10} {matches:^10} {lives:^10}")
    print(Style.RESET_ALL)

def set_ongoing_match():
    # Have the player type the indeces of two players and save it as an ongoing match
    # Check if the pairing is legal (i.e. neither player is already in a match)
    print("Who is the first player?")
    player1Index = input()
    print("Who is the second player?")
    player2Index = input()

    if not player1Index.isdigit() or not player2Index.isdigit():
        print(Fore.RED + "Please enter integers")
        print(Style.RESET_ALL)
        return

    player1Index = int(player1Index)
    player2Index = int(player2Index)
    if not (player1Index < len(players)) or not (player2Index < len(players)):
        print(Fore.RED + "Those player numbers are out of range")
        print(Style.RESET_ALL)
        return
    elif players[player1Index][1] == 0 or players[player2Index][1] == 0:
        print(Fore.RED + "Only players with lives can enter matches")
        print(Style.RESET_ALL)
        return
    elif player1Index == player2Index:
        print(Fore.RED + "The two players must be different")
        print(Style.RESET_ALL)
        return        

    for match in ongoingMatches:
        if (player1Index in match) or (player2Index in match):
            print(Fore.RED + "One of those players is already in an ongoing match")
            print(Style.RESET_ALL)
            return

    ongoingMatches.append([player1Index, player2Index])
    print(Fore.GREEN + "The match between " + str(player1Index) + " and " + str(player2Index) + " has been added!")
    print(Style.RESET_ALL)

def display_ongoing_matches():
    print(Fore.YELLOW + f"{"Index":^5}" + f"{"Matchup":^20}")
    for matchIndex in range(len(ongoingMatches)):
        print(f"{str(matchIndex):^5}" + f"{str(ongoingMatches[matchIndex][0]) + " is facing " + str(ongoingMatches[matchIndex][1]):^20}")
    print(Style.RESET_ALL)

def set_match_result():
    # List the ongoing matches with indeces and ask the player which to resolve
    display_ongoing_matches()
    print("Which match would you like to resolve?")
    matchChoice = input()
    if not matchChoice.isdigit():
        print(Fore.RED + "That was not a number")
        print(Style.RESET_ALL)
        return
    matchChoice = int(matchChoice)
    if not matchChoice < len(ongoingMatches):
        print(Fore.RED + "That Index is out of range")
        print(Style.RESET_ALL)
        return

    match = ongoingMatches[matchChoice]
    print("Which player won this match?")
    playerChoice = input()
    if not playerChoice.isdigit():
        print(Fore.RED + "That was not a number")
        print(Style.RESET_ALL)
        return
    playerChoice = int(playerChoice)
    if not playerChoice in match:
        print(Fore.RED + "That player is not in this match")
        print(Style.RESET_ALL)
        return
    
    # Set the winner of the match and alter the involved player values
    winIndex = playerChoice

    loseIndex = 0
    if winIndex == match[0]:
        loseIndex = match[1]
    else:
        loseIndex = match[0]
    
    #Handle the win
    players[winIndex][0]+=1

    #Handle the loss
    players[loseIndex][0]+=1
    players[loseIndex][1]-=1

    #Handle the match
    completeMatches.append([winIndex, loseIndex])
    ongoingMatches.pop(matchChoice)



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
# Helper functions
# def int_to_letter(value):
#     # Maps integers to capital letters. 0 to A, 1 to B, etc.
#     #!!! Values greater than 25 will no longer be letters
#     return chr(value + ord("A"))

if __name__=='__main__':
    main()