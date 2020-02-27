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



#create empty list for passing into GET_GAME_LIST function
gameDict = {}
GET_GAME_LIST(gameDict)

gameList = []
gameIdList = []
for key in gameDict:
    gameList.append(gameDict[key])
    gameIdList.append(key)


#set initial GAME_ID to first gameID in the list

GAME_ID=0
#function to set gameID to label clicked
def SET_GAME_ID(eff=None, id=0):
    global GAME_ID
    GAME_ID = id
    print(GAME_ID)

def setGameId(eff=None, gameDict=0):
    print(gameDict)


#create frame for displaying today's games in grid form
top = Frame(root, bg='#9e9e9e')
top.pack(fill=X, pady=2)
topBackgroundFrame = Frame(top)
topBackgroundFrame.pack(side=TOP, pady=2)
frameTop = Frame(topBackgroundFrame)
frameTop.grid(row=0,columnspan=len(gameList))

#create empty list for storing labels
gameLabels = []

#pupulate top frame with game labels using info from gameDict
i = 0
for game in gameDict:
    bg = "white"
    id = game
    if (i)%2 != 0:
        bg = "white"
    l = Label(frameTop, bd=4, relief=RIDGE, text=gameDict[game], bg=bg, font='Georgia', justify=LEFT, width=10, height=5)
    gameLabels.append(l)
    gameLabels[i].grid(row=0,column=i)
    #gameLabels[i].bind("<1>", lambda eff: SET_GAME_ID(eff,i))

    print(id)
    i = i+1


activeGame = gameList[0]

mainBackgroundFrame = Frame(root)
mainBackgroundFrame.pack()

frameLeft = Frame(mainBackgroundFrame)
frameLeft.grid(row=1, column=0, padx=10)
labelLeft = []
for i in range(0,5):
    l = Label(frameLeft,padx=20,relief=SUNKEN,bd=1,text='Player'+str(i+1))
    labelLeft.append(l)
    labelLeft[i].grid(row=(i))


frameMiddle = Frame(mainBackgroundFrame, width=1200, height=600)
frameMiddle.grid(row=1, column=1)
scoreboardLabel = Label(frameMiddle, text=activeGame, font=('Helvetica', 30), bg='black', fg='yellow', width=66, height=15)
scoreboardLabel.grid()


frameRight = Frame(mainBackgroundFrame)
frameRight.grid(row=1, column=2, padx=10)
labelRight = []
for i in range(0,5):
    l = Label(frameRight,padx=20,relief=SUNKEN,bd=1,text='Player'+str(i+1))
    labelRight.append(l)
    labelRight[i].grid(row=(i))



#what's happening right now is the variable 'id' in the loop above is being used to set the gameId
#the problem is by the time the program is running, the loop is finished and 'id' is set to the final gameID in the List
#need to figure out a way to return the id of the label that is being clicked
#i = 0
#for key in gameDict:
#    id = key
#    gameLabels[i].bind("<1>", lambda eff: setGameId(eff,key))
#    print("setting label id to " + str(key))
#    time.sleep(0.5)
#    i = i+1


gameLabels[0].bind("<1>", lambda eff: SET_GAME_ID(eff,1))
gameLabels[1].bind("<1>", lambda eff: SET_GAME_ID(eff,2))
#gameLabels[2].bind("<1>", setGameId(gameDict))


def test(num):
    print(num)

#def setScoreboard(num):


for i in range(0, len(gameDict)):
    gameLabels[i].bind("<1>", test(gameIdList[i]))

i = 0
for game in gameDict:
    print(game)
    print(gameIdList[i])
    i = i+1


#create callback function to display game of clicked label
#if a label is clicked, the game id will be returned to a current game id variable
#this variable will be used to display game information on the scoreboard



while True:
    root.update_idletasks()
    root.update()
    time.sleep(0.01)

#print(gameList)
