import requests

#api key RGAPI-c87cc474-d6d0-493e-b33b-3ec7869b2201

def championNameByID(id):
    URL = "http://ddragon.leagueoflegends.com/cdn/10.6.1/data/en_US/champion.json"
    response = requests.get(URL).json()
    allChampions = response['data']
    for champion in allChampions:
        if id == allChampions[champion]['key']:
            championName = allChampions[champion]['name']
            return championName

def requestSummonerData(region, summonerName):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=RGAPI-c87cc474-d6d0-493e-b33b-3ec7869b2201"
    response = requests.get(URL)
    return response.json()

def requestLastMatch(region, accountID):
   
    URL = "https://" + region + ".api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountID + "?api_key=RGAPI-c87cc474-d6d0-493e-b33b-3ec7869b2201"
    response = requests.get(URL)
    return response.json()
    
def requestRankData(region, accountID):
    URL =  "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + accountID + "?api_key=RGAPI-c87cc474-d6d0-493e-b33b-3ec7869b2201"
    response = requests.get(URL)
    return response.json()

def main():
    
    print("Enter your regions from the following\nNA1 EUW1 EUN LA1 LA2 OCE RU TR1 JP1 KR PBE")
    region = input("Region: ")
    summonerName = input("Summoner name: ")

    accountInfoJSON  = requestSummonerData(region, summonerName)
    ID = accountInfoJSON['id']
    ID = str(ID)
    accountID = accountInfoJSON['accountId']
    accountID = str(accountID)
    summonerID = accountInfoJSON['id']
    summonerID = str(summonerID)
    
    rankDataJSON = requestRankData(region, summonerID)

    print("Level: " + str(accountInfoJSON['summonerLevel']))

    if(rankDataJSON == []):
        print("Rank: Not ranked")
    else:
        tier = rankDataJSON[0]['tier']
        rank = rankDataJSON[0]['rank']
        lp = rankDataJSON[0]['leaguePoints']
        win = rankDataJSON[0]['wins']
        loss = rankDataJSON[0]['losses']
        winrate = win/(win + loss)
        print("Rank: " + str(tier) + " " + str(rank) + "\nLP: " + str(lp) + "\nWin Rate: " + str(winrate))



main()