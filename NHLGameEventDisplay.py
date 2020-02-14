#Testing API access https://from statsapi.web.nhl.com/api/v1

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

#strip the 0's in the players' numbers
homeRoster = map(lambda each:each.strip("0"), homeRoster)
awayRoster = map(lambda each:each.strip("0"), awayRoster)
jprint(homeRoster)
jprint(awayRoster)

liveData = eventlog['liveData']['plays']['allPlays']
mostRecentEvent = ''
onIce = []
while True:
    response = requests.get("https://statsapi.web.nhl.com/api/v1/game/2019020864/feed/live")
    eventlog = response.json()
    liveData = eventlog['liveData']['plays']['allPlays']

    for data in liveData:
        period = data['about']['ordinalNum']
        timeLeft = data['about']['periodTimeRemaining']
        event = data['result']['event']
        description = data['result']['description']
        awayScore = str(data['about']['goals']['away'])
        homeScore = str(data['about']['goals']['home'])
        gameScore = '[CGY: ' + awayScore + ' SJS: ' + homeScore + ']'

    newEvent = gameScore + ' ' + timeLeft + ' ' + period + ' - ' + event + ': ' + description
    #time.sleep(2)
    #print(newEvent)
    if mostRecentEvent != newEvent:
        print(newEvent)
    else:
        time.sleep(0.1)
    mostRecentEvent = newEvent

    boxScore = eventlog['liveData']['boxscore']
    onIceId = boxScore['teams']['home']['onIce']

    #need to change the indeces below, currently throws error when team is shorthanded due to list having length of 5 (instead of 6 at 5v5)
    newOnIce = [vanRos[onIceId[0]], vanRos[onIceId[1]], vanRos[onIceId[2]], vanRos[onIceId[3]], vanRos[onIceId[4]], vanRos[onIceId[5]]]
    if onIce != newOnIce:
        print(newOnIce)
    else:
        time.sleep(0.1)
    onIce = newOnIce

    #print(gameScore + ' ' + timeLeft + ' ' + period + ' - ' + event + ': ' + description)
#jprint(liveData)
