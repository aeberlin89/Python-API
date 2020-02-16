#Testing API access https://from statsapi.web.nhl.com/api/v1
#idea is to eventually access any current NHL game and display the score along with other important info
#info would then be displayed on remote screen (via RaspPI)
#default game would be stlblues, with option to change game info in some fashion (touchscreen, autoscroll, etc)

import requests
import json
import time


def jprint(obj):
    text=json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("https://statsapi.web.nhl.com/api/v1/game/2019020864/feed/live")
eventlog = response.json()
gameData = eventlog['gameData']
players = gameData['players']

#keys in 'players' dict are unknown ID numbers, and their value contains the info needed
#so playerData is created as a list containing dicts with that info
playerData = players.values()


homeTeamId = gameData['teams']['home']['id']
awayTeamId = gameData['teams']['away']['id']

homeRoster = []
awayRoster = []

for player in playerData:
    playerNumber = player['primaryNumber']
    #check for single digit numbers
    if len(playerNumber) == 1:
        #turn single digit numbers to double digits for sorting purposes
        playerNumber = '0' + playerNumber

    playerName = playerNumber + ' ' + player['firstName'] + ' ' + player['lastName']
    if player['currentTeam']['triCode'] == 'VAN':
        homeRoster.append(playerName)
    else:
        awayRoster.append(playerName)

#sort players according to number
homeRoster.sort()
awayRoster.sort()

#temporary dictionary containing a team's roster with associating player id's
# ***** need to either create new file containing all team's rosters OR
#need to look into creating separate request from team page with roster list
vanRos = { 8470626 : 'Loui Eriksson',
            8474849: 'Antoine Roussel',
            8474818: 'Jordie Benn',
            8477937: 'Jake Virtanen',
            8476468: 'J.T. Miller',
            8477967: 'Thatcher Demko',
            8471303: 'Alexander Edler',
            8476871: 'Tanner Pearson',
            8478874: 'Adam Gaudette',
            8477213: 'Tim Schaller',
            8480800: 'Quinn Hughes',
            8474574: 'Tyler Myers',
            8477500: 'Bo Horvat',
            8475690: 'Chris Tanev',
            8477473: 'Justin Bailer',
            8478465: 'Guillaume Brisebois',
            8479442: 'Troy Stecher',
            8479772: 'Zack MacEwen',
            8474593: 'Jacob Markstrom',
            8480012: 'Elias Pettersson',
            8474291: 'Jay Beagle',
            8474091: 'Brandon Sutter',
}

#dictionary of team id keys
#to access team roster statsapi.web.nhl.com/api/v1/teams/ + 'teamId' + /roster
teamId = {
    1: 'NJD', 2: 'NYI', 3: 'NYR', 4: 'PHI', 5: 'PIT', 6: 'BOS',
    7: 'BUF', 8: 'MTL', 9: 'OTT', 10: 'TOR', 12: 'CAR', 13: 'FLA',
    14: 'TBL', 15: 'WAS', 16: 'CHI', 17: 'DET', 18: 'NSH', 19: 'STL',
    20: 'CGY', 21: 'COL', 22: 'EDM', 23: 'VAN', 24: 'ANA', 25: 'DAL',
    26: 'LAK', 28: 'SJS', 29: 'CBJ', 30: 'MIN', 52: 'WPG', 53: 'ARI', 54: 'VGK'
}

hTeam = str(54)

#create strings to plug in current teams
homeURL = "https://statsapi.web.nhl.com/api/v1/teams/" + hTeam + "/roster"

homeTeam = requests.get(homeURL).json()
homRos = {}

for spot in homeTeam['roster']:
    playerID = spot['person']['id']
    playerFullName = spot['person']['fullName']
    homRos[playerID] = playerFullName
jprint(homRos)

#strip the 0's in the players' numbers
#homeRoster = map(lambda each:each.strip("0"), homeRoster)
#awayRoster = map(lambda each:each.strip("0"), awayRoster)

#print each team's active roster for the game
jprint(homeRoster)
jprint(awayRoster)

liveData = eventlog['liveData']['plays']['allPlays']

#create variables for storing info
mostRecentEvent = ''
onIce = []

#main loop
while True:
    response = requests.get("https://statsapi.web.nhl.com/api/v1/game/2019020864/feed/live")
    eventlog = response.json()
    liveData = eventlog['liveData']['plays']['allPlays']

    #loop retrieving all plays in the game and storing in data
    for data in liveData:
        #get period info (1,2,3, or OT)
        period = data['about']['ordinalNum']

        #get time remaining in period
        timeLeft = data['about']['periodTimeRemaining']

        #get event title ("SAVE", "FACEOFF", "GOAL", etc)
        event = data['result']['event']

        #get event description showing players involved
        description = data['result']['description']

        #score for each team
        awayScore = str(data['about']['goals']['away'])
        homeScore = str(data['about']['goals']['home'])

        #string to display current score of the game
        gameScore = '[CGY: ' + awayScore + ' SJS: ' + homeScore + ']'

    #store string with data retrieved from the request into a new string variable
    newEvent = gameScore + ' ' + timeLeft + ' ' + period + ' - ' + event + ': ' + description

    #compare events to see if a new event has occured
    #if so, the new event will print
    #if not, print nothing
    if mostRecentEvent != newEvent:
        print(newEvent)
        time.sleep(0.1)
    else:
        time.sleep(0.1)

    #store new event into most recent event for comparing next time through the loop
    mostRecentEvent = newEvent

    #get id number of players on the ice for each team
    boxScore = eventlog['liveData']['boxscore']
    homeOnIceId = boxScore['teams']['home']['onIce']
    awayOnIceId = boxScore['teams']['away']['onIce']
    newOnIce = []


    #for i in range(0,len(homeOnIceId)):


    #store on ice names in a string using roster dictionaries with player id's fetched above
    # ***** need to change the indeces below, currently throws error when team is shorthanded due to list having length of 5 (instead of 6 at 5v5)
    for i in range(0,len(homeOnIceId)):
        newOnIce.append(vanRos[homeOnIceId[i]])
    #newOnIce = [vanRos[homeOnIceId[0]], vanRos[homeOnIceId[1]], vanRos[homeOnIceId[2]], vanRos[homeOnIceId[3]], vanRos[homeOnIceId[4]], vanRos[homeOnIceId[5]]]
    if onIce != newOnIce:
        print(newOnIce)
    else:
        time.sleep(0.1)
    onIce = newOnIce
