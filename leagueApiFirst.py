import requests

#api key RGAPI-4ad87109-3779-4236-9f64-d5a52dd4cd6a

def requestSummonerData(region, summonerName, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

def requestLastMatch(region, accountID, APIKey):
   
    URL = "https://" + region + ".api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountID + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()
    
def requestRankData(region, accountID, APIKey):
    URL =  "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + accountID + "?api_key=" + APIKey
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