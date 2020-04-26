import requests
import urllib
#api key RGAPI-c87cc474-d6d0-493e-b33b-3ec7869b2201
"""
def championNameByID(id):
    URL = "http://ddragon.leagueoflegends.com/cdn/10.6.1/data/en_US/champion.json"
    response = requests.get(URL).json()
    allChampions = response['data']
    for champion in allChampions:
        if id == allChampions[champion]['key']:
            championName = allChampions[champion]['name']
            return championName
"""

def realRegion(region):
    if(region == 'na1' or region == 'euw1' or region == 'eun' or region == 'la1' or region == 'la2' or region == 'oce' or region == 'ru' or region == 'tr1' or region == 'jp1' or region == 'kr' or region == 'pbe'):
        return True
    else:
        return False

def requestSummonerData(region, summonerName):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=RGAPI-e3c3b304-de42-4d3c-ac83-90bc3be549ce"
    response = requests.get(URL)
    return response.json()
        
def requestLastMatch(region, accountID):
    URL = "https://" + region + ".api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountID + "?api_key=RGAPI-e3c3b304-de42-4d3c-ac83-90bc3be549ce"
    response = requests.get(URL)
    return response.json()
    
def requestRankData(region, accountID):
    URL =  "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + accountID + "?api_key=RGAPI-e3c3b304-de42-4d3c-ac83-90bc3be549ce"
    response = requests.get(URL)
    return response.json()



def main():
    x = 1
    
    while x != 0:
        print("Enter your regions from the following\nNA1 EUW1 EUN LA1 LA2 OCE RU TR1 JP1 KR PBE")
        region = input("Region: ")
        region = region.lower()
        if(realRegion(region)):
            summonerName = input("Summoner name: ")
            accountInfoJSON  = requestSummonerData(region, summonerName)

            if(accountInfoJSON == {"status":{"message":"Data not found - summoner not found","status_code":404}}):
                print("Account not found")
            else:
                ID = accountInfoJSON['id']
                ID = str(ID)
                accountID = accountInfoJSON['accountId']
                accountID = str(accountID)
                summonerID = accountInfoJSON['id']
                summonerID = str(summonerID)
            
                rankDataJSON = requestRankData(region, summonerID)

                print("Level: " + str(accountInfoJSON['summonerLevel']))

                if(rankDataJSON == []):
                    print("Rank: Unranked")
                else:
                    tier = rankDataJSON[0]['tier']
                    rank = rankDataJSON[0]['rank']
                    lp = rankDataJSON[0]['leaguePoints']
                    win = rankDataJSON[0]['wins']
                    loss = rankDataJSON[0]['losses']
                    winrate = win/(win + loss)
                    games = win + loss
                    print("Rank: " + str(tier) + " " + str(rank) + "\nLP: " + str(lp) + "\nWin Rate: " + str(winrate) + "\nGames Played: " + str(games))
        else:
            print("Region not found")

        answer = input("Would you like to quit the program (y/n)? ")
        while(x != 0):
            if(answer == 'y'):
                x = 0
                answer == ""
            elif(answer == 'n'):
                break
            else:
                print('Please enter y or n')
                answer = input("Would you like to quit the program (y/n)? ")
            





main()