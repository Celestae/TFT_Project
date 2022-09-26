import requests

api_key = "api_key=" + open("C:\\Users\\love-\\Documents\\tft_project_key_api.txt", "r").read()

class Player():
    #pass

    

    def __init__(self, summoner_name):
        self.summoner_name = summoner_name

    def get_matchid_with_puuid(self, puuid):
        api_url_matchid = "https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/" + puuid + "/ids?start=0&count=20&" + api_key
        response_matchid = requests.get(api_url_matchid).json()
        print(response_matchid)
        

    def get_puuid_with_summoner_name(self):
        
        # add your api_key

        api_url_summoner_name  = "https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/" + self.summoner_name  + "?" + api_key

        response_summoner_name = requests.get(api_url_summoner_name).json()
        puuid = response_summoner_name["puuid"]
        print(puuid)
        

        self.get_matchid_with_puuid(puuid)
    
    





Celestae = Player("Celestae")

print(Celestae.get_puuid_with_summoner_name())