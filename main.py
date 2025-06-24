from colorama import Fore, Back, Style
from functools import cmp_to_key
import copy
import random

players = [] # player = [matches, lives, name]
ongoingMatches = [] # match = [playerIndex1, playerIndex2]
completeMatches = [] # match = [playerIndexWin, playerIndexLose]

def main():
    # Show the main menu
    print(Style.RESET_ALL)
    print("Welcome to the Swiss Tournament Matchup Generator")
    auto_populate_players()
    menu()

def auto_populate_players():
    # Testing function to speed things up
    players.append([2, 0, 'A'])
    players.append([2, 1, 'B'])
    players.append([2, 2, 'C'])
    players.append([1, 2, 'D'])
    players.append([1, 1, 'E'])
    players.append([0, 2, 'F'])
    players.append([0, 2, 'G'])
    players.append([0, 2, 'H'])
    completeMatches.append([0,1])
    completeMatches.append([0,2])
    completeMatches.append([1,2])
    completeMatches.append([3,4])

def menu():
    keepgoing = True
    while keepgoing:
        print(Fore.MAGENTA)
        print("What would you like to do?")

        print("1) Add Players")
        print("2) Display Players\n")

        print("3) Generate Matchups\n")

        print("4) Set Ongoing Match")
        print("5) Display Ongoing Matches\n")

        print("6) Set Match Result")
        print("7) Display Match Results\n")

        print("0) Exit Program")
        print(Style.RESET_ALL)

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
                    display_players(list(range(len(players))))
                case 3:
                    generate_matchups_menu()
                case 4:
                    display_unoccupied_players()
                    set_ongoing_match()
                case 5:
                    display_ongoing_matches()
                case 6:
                    display_ongoing_matches()
                    set_match_result()
                case 7:
                    display_match_results()
                case 91:
                    secret_menu()
                case _:
                    print(Fore.RED + "That was not a valid option")
                    print(Style.RESET_ALL)
        else:
            print(Fore.RED + "That was not a valid option")
            print(Style.RESET_ALL)

# 1) Add Players
def add_players_menu():
    # Ask how many players the user wants to add
    print("How many players would you like to add?")
    numPlayers = input()
    if not numPlayers.isdigit():
        print(Fore.RED + "That was not a valid input")
        print(Style.RESET_ALL)
        return

    numPlayers = int(numPlayers)
    for i in range(numPlayers):
        add_player_menu()

    print(Fore.GREEN + str(numPlayers) + " players added successfully!")
    print(Style.RESET_ALL)
def add_player_menu():
    print("What is this player's name?")
    name = input()
    players.append([0, 2, name])

# 2) Display Players
def display_players(playerIndecesList):
    print(Fore.YELLOW + f"{"Index":^10} {"Name":^20} {"Matches":^10} {"Lives":^10}")
    for playerIndex in playerIndecesList:
        player = players[playerIndex]
        matches = player[0]
        name = player[2]
        lives = player[1]
        if lives == 0:
            print(Fore.RED + f"{playerIndex:^10} {name:^20} {matches:^10} {lives:^10}" + Fore.YELLOW)
        else:
            print(f"{playerIndex:^10} {name:^20} {matches:^10} {lives:^10}")
    print(Style.RESET_ALL)

# 3) Generate Matchups
def generate_matchups_menu():
    keepgoing = True
    while keepgoing:
        print(Fore.MAGENTA)
        print("What matchup would you like to generate?")
        print("1) Display Primed Players")
        print("2) Best Matchup\n")

        print("0) Exit Matchup Generation")
        print(Style.RESET_ALL)


        choice = input()
        if choice.isdigit():
            choice = int(choice)
            match choice:
                case 0:
                    keepgoing = False
                case 1:
                    display_primed_players()
                case 2:
                    best_matchup_menu()
                case _:
                    print("That was not a valid option")
        else:
            print("That was not a valid option")

def display_primed_players():
    # Sorts the list of players in order of primedness and prints it
    primedPlayerIndeces = list(range(len(players)))
    primedPlayerIndeces = sorted(primedPlayerIndeces, key=cmp_to_key(compare))

    print(Fore.YELLOW + f"{"Index":^10} {"Name":^20} {"Matches":^10} {"Lives":^10}")
    for playerIndex in primedPlayerIndeces:
        player = players[playerIndex]
        matches = player[0]
        name = player[2]
        lives = player[1]
        if lives == 0:
            print(Fore.RED + f"{playerIndex:^10} {name:^20} {matches:^10} {lives:^10}" + Fore.YELLOW)
        else:
            print(f"{playerIndex:^10} {name:^20} {matches:^10} {lives:^10}")
    print(Style.RESET_ALL)

def compare(p1Index, p2Index):
    # Returns -1 if p1 more primed, 1 if p2 more primed, 0 if equal
    p1 = players[p1Index]
    p2 = players[p2Index]
    matches1 = p1[0]
    matches2 = p2[0]
    lives1 = p1[1]
    lives2 = p2[1]

    if lives1 != 0 and lives2 == 0:
        return -1
    elif lives1 == 0 and lives2 != 0:
        return 1

    if matches1 < matches2:
        return -1
    elif matches1 > matches2:
        return 1

    if lives1 < lives2:
        return -1
    elif lives1 > lives2:
        return 1

    return 0

def best_matchup_menu():
    # Finds the best legal matchup, if possible. 
    # Lets the user remove one of the players in the found match to generate a new one

    excludeIndeces = []
    keepgoing = True
    while keepgoing:
        index1 = find_primed_player_index(excludeIndeces)
        index2 = find_primed_player_index(excludeIndeces, index1)
        if index1==-1 or index2==-1:
            print(Fore.RED + "No legal matchups exist!")
            print(Style.RESET_ALL)
            return
        print(f"{str(index1) + " " + players[index1][2] + " would face " + str(index2) + " " + players[index2][2]:^30}")

        print(Fore.MAGENTA)
        print("1) Remove Player 1")
        print("2) Remove Player 2\n")

        print("0) Exit matchup Menu")
        print(Style.RESET_ALL)

        choice = input()
        if choice.isdigit():
            choice = int(choice)
            match choice:
                case 0:
                    keepgoing = False
                case 1:
                    excludeIndeces.append(index1)
                case 2:
                    excludeIndeces.append(index2)
                case _:
                    print("That was not a valid option")
        else:
            print("That was not a valid option")

def find_primed_player_index(excludeIndeces = [], illegalPastOpponentIndex = -1):
    # Finds the player with the fewest matches and fewest lives that is alive, not in exlcudeIndeces, is not illegalPastOpponent, 
    # not in an ongoing match. Prioritize players that have not faced illegalPastOpponent, but it's okay if there are no other options.
    # If impossible, returns -1

    primedPlayerIndex = -1
    # Narrow down the list of possible players
    eligiblePlayerIndeces = list(range(len(players)))
    eligiblePlayerIndeces = get_living_players(eligiblePlayerIndeces)
    eligiblePlayerIndeces = get_unexcluded_players(eligiblePlayerIndeces, excludeIndeces)
    if illegalPastOpponentIndex != -1:
        eligiblePlayerIndeces = get_unexcluded_players(eligiblePlayerIndeces, [illegalPastOpponentIndex])
    eligiblePlayerIndeces = get_unoccupied_players(eligiblePlayerIndeces, ongoingMatches)
    if illegalPastOpponentIndex != -1:
        eligiblePlayerIndeces = get_fewest_times_played_opponent(eligiblePlayerIndeces, illegalPastOpponentIndex)

    # Find the most primed player of the remaining list
    if len(eligiblePlayerIndeces) > 0:
        # Get list of players with same matches and lives as most primed player in eligiblePlayers
        eligiblePlayerIndeces = sorted(eligiblePlayerIndeces, key=cmp_to_key(compare)) 

        bestEligiblePlayerIndeces = [eligiblePlayerIndeces[0]]
        bestMatches = players[eligiblePlayerIndeces[0]][0]
        bestLives = players[eligiblePlayerIndeces[0]][1]

        for playerIndex in eligiblePlayerIndeces:
            matches = players[playerIndex][0]
            lives = players[playerIndex][1]
            if matches == bestMatches and lives == bestLives:
                bestEligiblePlayerIndeces.append(playerIndex)
            else:
                break
        
        # Choose randomly from the remaining choices
        primedPlayerIndex = random.choice(bestEligiblePlayerIndeces)

    return primedPlayerIndex

def get_living_players(playerIndecesList):
    newPlayerIndecesList = []
    for playerIndex in playerIndecesList:
        player = players[playerIndex]
        lives = player[1]
        if lives < 1:
            continue
        newPlayerIndecesList.append(playerIndex)
    return newPlayerIndecesList
def get_unoccupied_players(playerIndecesList, ongoingMatchList):
    newPlayerIndecesList = []
    for playerIndex in playerIndecesList:
        isPlayerInMatch = False
        for match in ongoingMatchList:
            if playerIndex in match:
                isPlayerInMatch = True
                break
        if isPlayerInMatch:
            continue
        newPlayerIndecesList.append(playerIndex)
    return newPlayerIndecesList
def get_unexcluded_players(playerIndecesList, excludeIndeces):
    newPlayerIndecesList = []
    for playerIndex in playerIndecesList:
        if playerIndex in excludeIndeces:
            continue
        newPlayerIndecesList.append(playerIndex)
    return newPlayerIndecesList
def get_fewest_times_played_opponent(playerIndecesList, opponentIndex):
    # Returns the subset of playerIndecesList with the fewest number of times playing with opponentIndex in the past
    # If none have played, all are included in the output
    newPlayerIndecesList = []
    opponentMatches = []
    for match in completeMatches:
        if opponentIndex in match:
            opponentMatches.append(match)

    fewestMatches = 99
    for playerIndex in playerIndecesList:
        numMatches = 0
        for match in opponentMatches:
            if playerIndex in match:
                numMatches+=1
        if numMatches < fewestMatches:
            fewestMatches = numMatches
            newPlayerIndecesList = []
            newPlayerIndecesList.append(playerIndex)
        elif numMatches == fewestMatches:
            newPlayerIndecesList.append(playerIndex)

    return newPlayerIndecesList

# 4) Set Ongoing Match
def display_unoccupied_players():
    eligiblePlayers = list(range(len(players)))
    eligiblePlayers = get_living_players(eligiblePlayers)
    eligiblePlayers = get_unoccupied_players(eligiblePlayers, ongoingMatches)

    display_players(eligiblePlayers)

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
    print(Fore.GREEN + "The match between " + str(player1Index) + " " + players[player1Index][2] + " and " + str(player2Index) + " " + players[player2Index][2] + " has been added!")
    print(Style.RESET_ALL)

# 5) Display Ongoing Matches
def display_ongoing_matches():
    print(Fore.YELLOW + f"{"Index":^5}" + f"{"Matchup":^30}")
    for matchIndex in range(len(ongoingMatches)):
        p1Index = ongoingMatches[matchIndex][0]
        p1Name = players[p1Index][2]
        p2Index = ongoingMatches[matchIndex][1]
        p2Name = players[p2Index][2]
        print(f"{str(matchIndex):^5}" + f"{str(p1Index) + " " + p1Name + " is facing " + str(p2Index) + " " + p2Name:^30}")
    print(Style.RESET_ALL)

# 6) Set Match Result
def set_match_result():
    # Ask the player which to resolve
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

# 7) Display Match Results
def display_match_results():
    print(Fore.YELLOW + "Results")
    for match in completeMatches:
        p1Index = match[0]
        p1Name = players[p1Index][2]
        p2Index = match[1]
        p2Name = players[p2Index][2]
        print(f"{str(p1Index) + " " + p1Name + " defeated " + str(p2Index) + " " + p2Name:^30}")
    print(Style.RESET_ALL)



    # Display a list of every completed match in completeMatches
    # print(Fore.YELLOW)
    # for match in completeMatches:
    #     print(str(match[0]) + " defeated " + str(match[1]))
    # print(Style.RESET_ALL)


# 91) Secret Menu
def secret_menu():
    print(Fore.BLUE + "Welcome to the Secret Area!")

    keepgoing = True
    while keepgoing:
        print("What would you like to edit?")

        print("1) Player")
        print("2) Delete Player\n")

        print("3) Ongoing Matches")
        print("4) Delete Ongoing Match\n")

        print("5) Complete Matches")
        print("6) Delete Complete Match\n")

        print("0) Exit Secret Area")
        print("")

        choice = input()
        if choice.isdigit():
            choice = int(choice)
            match choice:
                case 0:
                    keepgoing = False
                    print(Style.RESET_ALL)
                case 1:
                    set_input_player_values()
                case 2:
                    delete_player()
                case 3:
                    set_input_ongoing_match_values()
                case 4:
                    delete_ongoing_match()
                case 5:
                    set_input_complete_match_values()
                case 6:
                    delete_complete_match()
                    
                case _:
                    print(Fore.RED + "That was not a valid option" + Fore.BLUE)
        else:
            print(Fore.RED + "That was not a valid option" + Fore.BLUE)

def set_input_player_values():
    display_players(list(range(len(players))))
    print(Fore.BLUE)

    print("Which player would you like to edit?")
    playerIndex = input()
    if not playerIndex.isdigit():
        print(Fore.RED + "That was not a valid input" + Fore.BLUE)
        return

    playerIndex = int(playerIndex)
    if not playerIndex < len(players):
        print(Fore.RED + "There are not that many players" + Fore.BLUE)
        return

    print("What is their new name?")
    name = input()
    players[playerIndex][2] = name

    print("What is their new 'Matches'?")
    matches = input()
    if not matches.isdigit():
        print(Fore.RED + "That was not a valid input" + Fore.BLUE)
        return
    players[playerIndex][0] = int(matches)

    print("What is their new 'Lives'?")
    lives = input()
    if not lives.isdigit():
        print(Fore.RED + "That was not a valid input" + Fore.BLUE)
        return
    players[playerIndex][1] = int(lives)

def delete_player(): #!!! Must alter indeces in matches when deleting player
    display_players(list(range(len(players))))
    print(Fore.BLUE)

    print("Which player would you like to delete?")
    playerIndex = input()
    if not playerIndex.isdigit():
        print(Fore.RED + "That was not a valid input" + Fore.BLUE)
        return

    playerIndex = int(playerIndex)
    if not playerIndex < len(players):
        print(Fore.RED + "There are not that many players" + Fore.BLUE)
        return
    
    players.pop(playerIndex)

def set_input_ongoing_match_values():
    display_ongoing_matches()
    print(Fore.BLUE)

    print("Which match would you like to edit?")
    matchIndex = input()
    if not matchIndex.isdigit():
        print(Fore.RED + "That was not a valid input" + Fore.BLUE)
        return

    matchIndex = int(matchIndex)
    if not matchIndex < len(ongoingMatches):
        print(Fore.RED + "There are not that many ongoing matches" + Fore.BLUE)
        return

    display_players(list(range(len(players))))
    print(Fore.BLUE)

    print("What is the first player's index?")
    p1Index = input()
    if not p1Index.isdigit():
        print(Fore.RED + "That was not a valid input" + Fore.BLUE)
        return
    print("What is the second player's index?")
    p2Index = input()
    if not p2Index.isdigit():
        print(Fore.RED + "That was not a valid input" + Fore.BLUE)
        return

    ongoingMatches[matchIndex] = [int(p1Index), int(p2Index)]

def delete_ongoing_match():
    display_ongoing_matches()
    print(Fore.BLUE)

    print("Which match would you like to delete?")
    matchIndex = input()
    if not matchIndex.isdigit():
        print(Fore.RED + "That was not a valid input" + Fore.BLUE)
        return

    matchIndex = int(matchIndex)
    if not matchIndex < len(ongoingMatches):
        print(Fore.RED + "There are not that many ongoing matches" + Fore.BLUE)
        return
    
    ongoingMatches.pop(matchIndex)

def set_input_complete_match_values():
    display_match_results() #!!! Need to show indeces
    print(Fore.BLUE)

    print("Which match would you like to edit?")
    matchIndex = input()
    if not matchIndex.isdigit():
        print(Fore.RED + "That was not a valid input" + Fore.BLUE)
        return

    matchIndex = int(matchIndex)
    if not matchIndex < len(completeMatches):
        print(Fore.RED + "There are not that many complete matches" + Fore.BLUE)
        return

    display_players(list(range(len(players))))
    print(Fore.BLUE)

    print("What is the winning player's index?")
    p1Index = input()
    if not p1Index.isdigit():
        print(Fore.RED + "That was not a valid input" + Fore.BLUE)
        return
    print("What is the losing player's index?")
    p2Index = input()
    if not p2Index.isdigit():
        print(Fore.RED + "That was not a valid input" + Fore.BLUE)
        return

    completeMatches[matchIndex] = [int(p1Index), int(p2Index)]

def delete_complete_match():
    display_match_results() #!!! Need to show indeces
    print(Fore.BLUE)

    print("Which match would you like to delete?")
    matchIndex = input()
    if not matchIndex.isdigit():
        print(Fore.RED + "That was not a valid input" + Fore.BLUE)
        return

    matchIndex = int(matchIndex)
    if not matchIndex < len(ongoingMatches):
        print(Fore.RED + "There are not that many complete matches" + Fore.BLUE)
        return
    
    completeMatches.pop(matchIndex)


if __name__=='__main__':
    main()