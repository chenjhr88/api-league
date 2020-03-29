import requests

#api key RGAPI-c87cc474-d6d0-493e-b33b-3ec7869b2201

def requestSummonerData(region, summonerName, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=RGAPI-c87cc474-d6d0-493e-b33b-3ec7869b2201"
    response = requests.get(URL)
    return response.json()

def requestLastMatch(region, accountID, APIKey):
   
    URL = "https://" + region + ".api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountID + "?api_key=RGAPI-c87cc474-d6d0-493e-b33b-3ec7869b2201"
    response = requests.get(URL)
    return response.json()
    
def requestRankData(region, accountID, APIKey):
    URL =  "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + accountID + "?api_key=RGAPI-c87cc474-d6d0-493e-b33b-3ec7869b2201"
    response = requests.get(URL)
    return response.json()

def main():
    print("Enter your regions from the following\nNA1 EUW1 EUN LA1 LA2 OCE RU TR1 JP1 KR PBE")
    region = input("Region: ")
    summonerName = input("Summoner name: ")
    APIKey = input("API Key: ")

    responseJSON  = requestSummonerData(region, summonerName, APIKey)
    ID = responseJSON['id']
    ID = str(ID)
    accountID = responseJSON['accountId']
    accountID = str(accountID)

main()