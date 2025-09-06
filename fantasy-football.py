RIVAL_WEEK_1 = 1
RIVAL_WEEK_2 = 7
RIVAL_WEEK_3 = 14

def createSchedule():

    #Getting information about the league
    evenTeams = False
    while not evenTeams:
        numTeams = int(input("Please enter the number of teams in the league: "))
        if numTeams % 2 == 0:
            evenTeams = True

    numWeeks = int(input("Please enter the number of regular season weeks: "))

    enableRivals = False
    if input("Type \"Yes\" to enable rivalries: ") == "Yes":
        enableRivals = True
    
    if enableRivals:
        input("Next, you will be prompted to enter the name of each team. Do this in rival pairs\nEx. If John and Bob were rivals, you would type John on the first prompt followed by Bob on the next prompt.\nClick enter to continue")
    else:
        input("Next, you will be prompted to enter the name of each team. Click enter to continue.")

    #Initializing teams and circular list 
    teams = []
    count = 0
    while count < numTeams:
        teams.append(input("Enter team #" + str(count+1) + ": "))
        count += 1
    
    print(teams)
    print(len(teams))

    if enableRivals:
        offset = 1
        while offset < len(teams)/2:
            teams.append(teams.pop(len(teams)-(offset*2)-1))
            offset += 1

    teamsCircular = teams.copy()

    #Start schedule creation    
    print("\nGenerating schedule...\n")

    #Setup variables
    currWeek = 1
    offset = 0

    #Each week of matchups
    while currWeek <= numWeeks:
        print("Week " + str(currWeek) + " -------------------------------------------")
        
        if (currWeek == RIVAL_WEEK_1 or currWeek == RIVAL_WEEK_2 or currWeek == RIVAL_WEEK_3) and enableRivals:
            teamsCopy = teams.copy()
        else:
            teamsCopy = teamsCircular.copy()
        
        counter = 0

        #Each game in the week
        while(counter < len(teams)/2):
            playerOne = teamsCopy[0]
            playerTwo = teamsCopy[len(teamsCopy)-1]

            print("Matchup " + str(counter+1) + ": " + playerOne + " vs " + playerTwo)

            teamsCopy.remove(playerOne)
            teamsCopy.remove(playerTwo)

            counter += 1
        currWeek += 1
        offset += 1

        if not ((currWeek == RIVAL_WEEK_1 or currWeek == RIVAL_WEEK_2 or currWeek == RIVAL_WEEK_3) and enableRivals):
            #Shift circular list
            teamsCircular.append(teamsCircular.pop(1))
        
        if enableRivals and teams[1] == teamsCircular[1]:
            teamsCircular.append(teamsCircular.pop(1))

createSchedule()
