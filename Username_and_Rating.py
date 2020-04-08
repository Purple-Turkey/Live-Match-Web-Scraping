import requests
from bs4 import BeautifulSoup

gamesplayed = {}
usernamelist = ''
def AltStart1(a):
    return a[::2]
def AltStart2(b):
    return b[1::2]

print('Usernames\n')
for x in range(5957, 5955, -1):
    VaryingURL = 'htt' + 'ps://www.chess.com/club/matches/live/' + str(x) + '/games'
    allwords = requests.get(VaryingURL)
    soup = BeautifulSoup(allwords.content, 'html.parser')
    sometitle = soup.title.text
    if sometitle.find('ustralia') >= 0 and sometitle.find('LCWL S5') >= 0 and sometitle.find('U1600') == -1:
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
                    print(username)
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
                    print(username)
                    usernamelist += str(username) + ' '
                    gamesplayed[username] = vars()[uservariable]
    else:
        continue

def Listify(string):
    li = list(string.split(" ")) 
    return li

betterlist = Listify(usernamelist)
del betterlist[-1]

print('\nNumber of Matches Played in\n')
for player in betterlist:
    print(gamesplayed.get(player))

print('\nExcel Usernames\n')
for player in betterlist:
    print('=\"@' + player + '\"')

print('\nChess.com Linked Usernames\n')
for player in betterlist:
    print('@' + player)


print('\nBlitz Ratings\n')
for username in betterlist:
    bulletrating = -47
    StatsURL = 'https'+'://www.chess.com/stats/live/blitz/'+ username
    Statswords = requests.get(StatsURL)
    Statssoup = BeautifulSoup(Statswords.content, 'html.parser')
    Statratings = Statssoup.find_all(class_='user-rating')
    for rating in Statratings:
        isitgoodrating = rating.parent.text.strip()
        if isitgoodrating.find('Blitz') >= 0:
            bulletrating = int(rating.text.strip())
            print(bulletrating)
    if bulletrating == -47:
        print('0')

print('\nBullet Ratings\n')
for username in betterlist:
    bulletrating = -47
    StatsURL = 'https'+'://www.chess.com/stats/live/blitz/'+ username
    Statswords = requests.get(StatsURL)
    Statssoup = BeautifulSoup(Statswords.content, 'html.parser')
    Statratings = Statssoup.find_all(class_='user-rating')
    for rating in Statratings:
        isitgoodrating = rating.parent.text.strip()
        if isitgoodrating.find('Bullet') >= 0:
            bulletrating = int(rating.text.strip())
            print(bulletrating)
    if bulletrating == -47:
        print('0')

print('\nRapid Ratings\n')
for username in betterlist:
    bulletrating = -47
    StatsURL = 'https'+'://www.chess.com/stats/live/blitz/'+ username
    Statswords = requests.get(StatsURL)
    Statssoup = BeautifulSoup(Statswords.content, 'html.parser')
    Statratings = Statssoup.find_all(class_='user-rating')
    for rating in Statratings:
        isitgoodrating = rating.parent.text.strip()
        if isitgoodrating.find('Rapid') >= 0:
            bulletrating = int(rating.text.strip())
            print(bulletrating)
    if bulletrating == -47:
        print('0')