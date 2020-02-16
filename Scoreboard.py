from tkinter import *
import requests
import json
import time

root = Tk()

TEAM_ID = {
    1: 'NJD', 2: 'NYI', 3: 'NYR', 4: 'PHI', 5: 'PIT', 6: 'BOS',
    7: 'BUF', 8: 'MTL', 9: 'OTT', 10: 'TOR', 12: 'CAR', 13: 'FLA',
    14: 'TBL', 15: 'WAS', 16: 'CHI', 17: 'DET', 18: 'NSH', 19: 'STL',
    20: 'CGY', 21: 'COL', 22: 'EDM', 23: 'VAN', 24: 'ANA', 25: 'DAL',
    26: 'LAK', 28: 'SJS', 29: 'CBJ', 30: 'MIN', 52: 'WPG', 53: 'ARI', 54: 'VGK'
}

def GET_GAME_LIST(game_dict):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/schedule")
    log = response.json()
    games = log['dates'][0]['games']
    for game in games:
        gameId = game['gamePk']
        status = game['status']['abstractGameState']
        awayTeamId = game['teams']['away']['team']['id']
        homeTeamId = game['teams']['home']['team']['id']
        game_dict[gameId] = status + '\n\n' + TEAM_ID[awayTeamId] + '\n' + TEAM_ID[homeTeamId]
        #empty_list.append(status + '\n\n' + TEAM_ID[awayTeamId] + '\n' + TEAM_ID[homeTeamId])

def getGameListID(game_dict):
    list = []
    for key in game_dict.keys():
        list.append(key)
    return list

#create empty list for passing into GET_GAME_LIST function
gameDict = {}
GET_GAME_LIST(gameDict)

gameList = []
for key in gameDict:
    gameList.append(gameDict[key])


#set initial GAME_ID to first gameID in the list

GAME_ID=0
#function to set gameID to label clicked
def SET_GAME_ID(eff=None, id=0):
    global GAME_ID
    GAME_ID = id
    print(GAME_ID)

#create frame for displaying today's games in grid form
frameTop = Frame(root)
frameTop.grid(columnspan=len(gameList), sticky='n')

#create empty list for storing labels
gameLabels = []

#pupulate top frame with game labels using info from gameDict
i = 0
for game in gameDict:
    bg = "white"
    id = game
    if (i)%2 != 0:
        bg = "light gray"
    l = Label(frameTop, bd=2, relief='solid', text=gameDict[game], bg=bg, font='Georgia', justify=LEFT, width=10, height=5)
    gameLabels.append(l)
    gameLabels[i].grid(row=0,column=i)
    #gameLabels[i].bind("<1>", lambda eff: SET_GAME_ID(eff,i))

    print(id)
    i = i+1

gameListID = getGameListID(gameDict)

i = 0
for i in range(0, len(gameListID)):
    gameLabels[i].bind("<1>",lambda eff: SET_GAME_ID(eff,gameListID[i]))

print(gameListID)



#what's happening right now is the variable 'id' in the loop above is being used to set the gameId
#the problem is by the time the program is running, the loop is finished and 'id' is set to the final gameID in the List
#need to figure out a way to return the id of the label that is being clicked





#create callback function to display game of clicked label
#if a label is clicked, the game id will be returned to a current game id variable
#this variable will be used to display game information on the scoreboard





while True:
    root.update_idletasks()
    root.update()
    time.sleep(0.5)

#print(gameList)
