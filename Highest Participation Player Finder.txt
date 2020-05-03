import requests
from bs4 import BeautifulSoup

gamesplayed = {}
usernamelist = ''
highestnogames = [-1]
def AltStart1(a):
    return a[::2]
def AltStart2(b):
    return b[1::2]

URLslist = ['https://www.chess.com/club/matches/live/team-australia/9802', 'https://www.chess.com/club/matches/live/team-australia/8512', 'https://www.chess.com/club/matches/live/team-australia/7156/games', 'https://www.chess.com/club/matches/live/team-australia/6799/games', 'https://www.chess.com/club/matches/live/team-australia/6610/games', 'https://www.chess.com/club/matches/live/team-australia/6309/games', 'https://www.chess.com/club/matches/live/team-australia/6195/games', 'https://www.chess.com/club/matches/live/team-australia/6058/games', 'https://www.chess.com/club/matches/live/team-australia/5956/games']
for VaryingURL in URLslist:
    allwords = requests.get(VaryingURL)
    soup = BeautifulSoup(allwords.content, 'html.parser')
    sometitle = soup.title.text
    ateam = soup.find(class_='clubs-team-match-name')
    players = soup.find_all(class_='post-view-meta-username v-user-popover')
    if ateam.text.find('Team Australia') >= 0:
        for player in AltStart1(players):
            username = player.text.strip()
            if username in usernamelist:
                uservariable = str(username) + 'person'
                vars()[uservariable] += 1
                gamesplayed[username] = vars()[uservariable]
            else:
                uservariable = str(username) + 'person'
                vars()[uservariable] = 1
                usernamelist += str(username) + ' '
                gamesplayed[username] = vars()[uservariable]
    else:
        for player in AltStart2(players):
            username = player.text.strip()
            if username in usernamelist:
                uservariable = str(username) + 'person'
                vars()[uservariable] += 1
                gamesplayed[username] = vars()[uservariable]
            else:
                uservariable = str(username) + 'person'
                vars()[uservariable] = 1
                usernamelist += str(username) + ' '
                gamesplayed[username] = vars()[uservariable]

def Listify(string):
    li = list(string.split(" ")) 
    return li

betterlist = Listify(usernamelist)
del betterlist[-1]

print('\nPlayer(s) with Highest Participation\n')

max_value = max(gamesplayed.values())
max_keys = [k for k, v in gamesplayed.items() if v == max_value]

print(max_value, max_keys)